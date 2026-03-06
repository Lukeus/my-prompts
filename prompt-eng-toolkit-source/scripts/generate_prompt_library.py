#!/usr/bin/env python3
"""
Generate an adapted prompt library for a target repository.

This script scans a codebase, selects the relevant prompt categories,
adapts placeholders with project-specific defaults, and writes the
resulting library plus support files to a destination directory.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from adapt_prompts import adapt_template, build_replacements
from scan_codebase import build_profile, to_yaml_string


ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_LIBRARY_DIR = ROOT_DIR / "prompt-library"
DEFAULT_SETUP_TEMPLATE = ROOT_DIR / "prompt-eng-toolkit-source" / "assets" / "SETUP_TEMPLATE.md"

CATEGORY_ORDER = [
    "data-engineering",
    "software-development",
    "ui-development",
    "prompt-refinement",
    "codebase-research",
]

CATEGORY_TITLES = {
    "data-engineering": "Data Engineering",
    "software-development": "Software Development",
    "ui-development": "UI Development",
    "prompt-refinement": "Prompt Refinement",
    "codebase-research": "Codebase Research",
}

SECTION_TITLES = {
    "templates": "Templates",
    "playbooks": "Playbooks",
    "stack-specific": "Stack-Specific",
    "exploration": "Exploration",
    "documentation": "Documentation Generation",
}

TOOL_NOTES = {
    "claude": "This output targets Claude Code. Prompts in `.claude/prompts/` are available as project context.",
    "copilot": "This output targets GitHub Copilot. Prompts in `.github/copilot/prompts/` can be referenced from Copilot Chat.",
    "cursor": "This output targets Cursor. Prompts in `.cursor/prompts/` integrate with Cursor's rules and context system.",
    "generic": "This output is tool-agnostic markdown. Any assistant that can read files from the repo can use it.",
}

STACK_SPECIFIC_RULES = {
    "data-engineering/stack-specific/dbt.md": lambda profile: "dbt" in profile.get("data_tools", []),
    "data-engineering/stack-specific/airflow-orchestration.md": lambda profile: "Apache Airflow" in profile.get("data_tools", []),
    "software-development/stack-specific/python.md": lambda profile: any(
        "Python" in language for language in profile.get("languages", [])
    ),
    "software-development/stack-specific/docker-devops.md": lambda profile: (
        profile.get("infrastructure", {}).get("has_docker", False)
        or profile.get("infrastructure", {}).get("ci_tool") != "none detected"
    ),
    "ui-development/stack-specific/react.md": lambda profile: any(
        framework in (
            profile.get("frontend", {}).get("frameworks", [])
            + profile.get("frameworks", [])
        )
        for framework in ("React", "Next.js")
    ),
    "codebase-research/stack-specific/monorepo-analysis.md": lambda profile: profile.get("architecture") == "monorepo",
}


def infer_tool(output_dir: Path, requested_tool: str | None) -> str:
    if requested_tool:
        return requested_tool

    normalized = output_dir.as_posix().lower()
    if "/.claude/" in normalized or normalized.endswith("/.claude") or normalized.endswith("/.claude/prompts"):
        return "claude"
    if "/.github/copilot/" in normalized or normalized.endswith("/.github/copilot/prompts"):
        return "copilot"
    if "/.cursor/" in normalized or normalized.endswith("/.cursor") or normalized.endswith("/.cursor/prompts"):
        return "cursor"
    return "generic"


def select_categories(profile: dict, include_all: bool) -> list[str]:
    if include_all:
        return CATEGORY_ORDER[:]

    categories = ["prompt-refinement", "codebase-research"]

    has_data = bool(
        profile.get("databases")
        or profile.get("data_tools")
        or profile.get("structure", {}).get("has_migrations")
    )
    has_code = bool(
        profile.get("languages")
        or profile.get("frameworks")
        or profile.get("infrastructure", {}).get("has_docker")
        or profile.get("infrastructure", {}).get("ci_tool") != "none detected"
    )
    has_frontend = bool(profile.get("frontend", {}).get("detected"))

    if has_data:
        categories.insert(0, "data-engineering")
    if has_code:
        insert_at = 1 if "data-engineering" in categories else 0
        categories.insert(insert_at, "software-development")
    if has_frontend:
        insert_at = 2 if "software-development" in categories else 1 if "data-engineering" in categories else 0
        categories.insert(insert_at, "ui-development")

    return [category for category in CATEGORY_ORDER if category in categories]


def should_include_file(relative_path: Path, profile: dict, selected_categories: set[str]) -> bool:
    if relative_path.name in {"README.md", "INDEX.md"}:
        return False

    category = relative_path.parts[0]
    if category not in selected_categories:
        return False

    rule = STACK_SPECIFIC_RULES.get(relative_path.as_posix())
    if rule is not None:
        return rule(profile)

    return True


def select_prompt_files(library_dir: Path, profile: dict, include_all: bool) -> tuple[list[str], list[Path]]:
    categories = select_categories(profile, include_all)
    selected_categories = set(categories)
    files = []

    for md_file in sorted(library_dir.glob("**/*.md")):
        relative_path = md_file.relative_to(library_dir)
        if should_include_file(relative_path, profile, selected_categories):
            files.append(md_file)

    return categories, files


def summarize_profile(profile: dict, categories: list[str]) -> str:
    infrastructure = profile.get("infrastructure", {})

    summary_lines = [
        f"- Included categories: {', '.join(CATEGORY_TITLES[category] for category in categories)}",
        f"- Architecture: {profile.get('architecture', 'unknown')}",
        f"- Languages: {', '.join(profile.get('languages', [])) or 'none detected'}",
        f"- Frameworks: {', '.join(profile.get('frameworks', [])) or 'none detected'}",
    ]

    if profile.get("databases") or profile.get("data_tools"):
        summary_lines.append(
            "- Data stack: "
            + ", ".join(profile.get("databases", []) + profile.get("data_tools", []))
        )

    testing_frameworks = profile.get("testing", {}).get("frameworks", [])
    summary_lines.append(
        f"- Testing: {', '.join(testing_frameworks) or 'none detected'}"
    )
    infrastructure_items = [
        item
        for item in [
            "Docker" if infrastructure.get("has_docker") else "",
            "Kubernetes" if infrastructure.get("has_k8s") else "",
            infrastructure.get("ci_tool", "none detected"),
        ]
        if item and item != "none detected"
    ]
    summary_lines.append(
        f"- Infrastructure: {', '.join(infrastructure_items) or 'none detected'}"
    )

    return "\n".join(summary_lines)


def build_tree(paths: list[Path]) -> dict:
    tree: dict[str, dict | None] = {}

    for path in sorted(paths):
        node = tree
        parts = list(path.parts)
        for index, part in enumerate(parts):
            is_last = index == len(parts) - 1
            if is_last:
                node.setdefault(part, None)
            else:
                node = node.setdefault(part, {})

    return tree


def render_tree(tree: dict, prefix: str = "") -> list[str]:
    lines = []
    entries = sorted(tree.items(), key=lambda item: (item[1] is None, item[0]))

    for index, (name, child) in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "`-- " if is_last else "|-- "
        lines.append(f"{prefix}{connector}{name}")
        if isinstance(child, dict):
            extension = "    " if is_last else "|   "
            lines.extend(render_tree(child, prefix + extension))

    return lines


def build_directory_tree(output_dir: Path, selected_files: list[Path]) -> str:
    relative_paths = [
        path.relative_to(output_dir)
        for path in selected_files
    ]
    relative_paths.extend([
        Path("README.md"),
        Path("INDEX.md"),
        Path("_project-profile.yml"),
    ])
    root_name = output_dir.name or "prompts"
    lines = [root_name]
    lines.extend(render_tree(build_tree(relative_paths)))
    return "\n".join(lines)


def extract_prompt_metadata(source_path: Path) -> tuple[str, str]:
    title = source_path.stem.replace("-", " ").title()
    description = ""

    for line in source_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            title = title.replace(" Template", "").replace("-Specific Prompts", "")
        elif line.startswith("> "):
            description = line[2:].strip()
            break

    return title, description


def build_index_markdown(output_dir: Path, selected_files: list[Path], project_name: str) -> str:
    grouped: dict[str, dict[str, list[tuple[Path, str, str]]]] = defaultdict(lambda: defaultdict(list))

    for output_path in selected_files:
        relative_path = output_path.relative_to(output_dir)
        title, description = extract_prompt_metadata(output_path)
        category = relative_path.parts[0]
        section = relative_path.parts[1]
        grouped[category][section].append((relative_path, title, description))

    lines = [
        "# Adapted Prompt Library - Index",
        "",
        f"**{len(selected_files)} prompts** adapted for `{project_name}`.",
        "",
    ]

    for category in CATEGORY_ORDER:
        if category not in grouped:
            continue
        category_files = grouped[category]
        category_count = sum(len(items) for items in category_files.values())
        lines.append(f"## {CATEGORY_TITLES[category]} ({category_count} prompts)")
        lines.append("")

        for section in SECTION_TITLES:
            items = category_files.get(section)
            if not items:
                continue
            lines.append(f"### {SECTION_TITLES[section]}")
            for relative_path, title, description in items:
                line = f"- [{title}]({relative_path.as_posix()})"
                if description:
                    line += f" - {description}"
                lines.append(line)
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_setup_readme(
    setup_template_path: Path,
    profile: dict,
    categories: list[str],
    prompt_count: int,
    output_dir: Path,
    directory_tree: str,
    tool: str,
) -> str:
    template = setup_template_path.read_text(encoding="utf-8")
    replacements = {
        "{{PROJECT_NAME}}": profile.get("project_name", output_dir.parent.name),
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
        "{{PROMPT_COUNT}}": str(prompt_count),
        "{{STACK_SUMMARY}}": summarize_profile(profile, categories),
        "{{DIRECTORY_TREE}}": directory_tree,
        "{{PROMPT_DIR}}": output_dir.as_posix(),
        "{{TOOL_NOTE}}": TOOL_NOTES[tool],
    }

    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)

    return template


def generate_prompt_library(
    repo_path: Path,
    output_dir: Path,
    library_dir: Path = DEFAULT_LIBRARY_DIR,
    setup_template_path: Path = DEFAULT_SETUP_TEMPLATE,
    include_all: bool = False,
    tool: str | None = None,
) -> dict:
    repo_path = repo_path.resolve()
    output_dir = output_dir.resolve()
    library_dir = library_dir.resolve()
    setup_template_path = setup_template_path.resolve()

    profile = build_profile(repo_path)
    categories, template_files = select_prompt_files(library_dir, profile, include_all)
    replacements = build_replacements(profile)
    resolved_tool = infer_tool(output_dir, tool)

    output_dir.mkdir(parents=True, exist_ok=True)
    written_prompt_files = []

    for template_path in template_files:
        relative_path = template_path.relative_to(library_dir)
        output_path = output_dir / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        template_text = template_path.read_text(encoding="utf-8")
        adapted_text = adapt_template(template_text, replacements)
        output_path.write_text(adapted_text, encoding="utf-8")
        written_prompt_files.append(output_path)

    profile_output = output_dir / "_project-profile.yml"
    profile_output.write_text(to_yaml_string(profile) + "\n", encoding="utf-8")

    directory_tree = build_directory_tree(output_dir, written_prompt_files)
    readme_output = output_dir / "README.md"
    readme_output.write_text(
        render_setup_readme(
            setup_template_path=setup_template_path,
            profile=profile,
            categories=categories,
            prompt_count=len(written_prompt_files),
            output_dir=output_dir,
            directory_tree=directory_tree,
            tool=resolved_tool,
        ),
        encoding="utf-8",
    )

    index_output = output_dir / "INDEX.md"
    index_output.write_text(
        build_index_markdown(output_dir, written_prompt_files, profile.get("project_name", repo_path.name)),
        encoding="utf-8",
    )

    return {
        "profile": profile,
        "categories": categories,
        "prompt_count": len(written_prompt_files),
        "tool": resolved_tool,
        "output_dir": output_dir,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an adapted prompt library for a repository")
    parser.add_argument("--repo", required=True, help="Repository to scan and adapt prompts for")
    parser.add_argument("--output-dir", required=True, help="Directory to write the adapted prompts to")
    parser.add_argument("--library-dir", default=str(DEFAULT_LIBRARY_DIR), help="Source prompt library directory")
    parser.add_argument(
        "--setup-template",
        default=str(DEFAULT_SETUP_TEMPLATE),
        help="README template used for generated prompt libraries",
    )
    parser.add_argument(
        "--tool",
        choices=("claude", "copilot", "cursor", "generic"),
        help="Override tool-specific README note generation",
    )
    parser.add_argument("--include-all", action="store_true", help="Generate every prompt regardless of detected stack")

    args = parser.parse_args()

    result = generate_prompt_library(
        repo_path=Path(args.repo),
        output_dir=Path(args.output_dir),
        library_dir=Path(args.library_dir),
        setup_template_path=Path(args.setup_template),
        include_all=args.include_all,
        tool=args.tool,
    )

    print(f"Project: {result['profile'].get('project_name', 'unknown')}")
    print(f"Categories: {', '.join(result['categories'])}")
    print(f"Prompts written: {result['prompt_count']}")
    print(f"Tool mode: {result['tool']}")
    print(f"Output: {result['output_dir']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
