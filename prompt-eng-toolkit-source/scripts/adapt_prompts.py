#!/usr/bin/env python3
"""
Prompt Adapter for Prompt Engineering Toolkit

Takes a project profile (from scan_codebase.py) and a prompt template,
then replaces {{PLACEHOLDER}} values with project-specific defaults.

Usage:
    python adapt_prompts.py --profile profile.yml --template template.md --output adapted.md

Or adapt an entire directory:
    python adapt_prompts.py --profile profile.yml --template-dir references/ --output-dir prompts/
"""

import re
import sys
from pathlib import Path


def parse_simple_yaml(text: str) -> dict:
    """Minimal YAML parser for our profile format."""
    result = {}
    stack = [(result, -1)]

    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue

        # Measure indent
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Pop stack to find parent at correct indent level
        while len(stack) > 1 and stack[-1][1] >= indent:
            stack.pop()

        current = stack[-1][0]

        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()

            if not value:
                # Nested dict
                new_dict = {}
                if isinstance(current, dict):
                    current[key] = new_dict
                stack.append((new_dict, indent))
            elif value.startswith("[") and value.endswith("]"):
                # Inline list
                items = [v.strip() for v in value[1:-1].split(",") if v.strip()]
                if isinstance(current, dict):
                    current[key] = items
            elif value.lower() in ("true", "false"):
                if isinstance(current, dict):
                    current[key] = value.lower() == "true"
            else:
                if isinstance(current, dict):
                    current[key] = value
        elif stripped.startswith("- "):
            item = stripped[2:].strip()
            if isinstance(current, dict):
                # Find the last key that should be a list
                for k in reversed(list(current.keys())):
                    if isinstance(current[k], list):
                        current[k].append(item)
                        break
                    elif isinstance(current[k], dict) and not current[k]:
                        current[k] = [item]
                        break

    return result


def build_replacements(profile: dict) -> dict:
    """Build a mapping of {{PLACEHOLDER}} -> value from the profile."""
    languages = profile.get("languages", [])
    frameworks = profile.get("frameworks", [])
    databases = profile.get("databases", [])
    data_tools = profile.get("data_tools", [])
    testing = profile.get("testing", {})
    test_frameworks = testing.get("frameworks", []) if isinstance(testing, dict) else []
    infra = profile.get("infrastructure", {})
    frontend = profile.get("frontend", {})
    conventions = profile.get("conventions", {})

    primary_lang = languages[0] if languages else "{{LANGUAGE}}"
    primary_framework = frameworks[0] if frameworks else "{{FRAMEWORK}}"
    primary_db = databases[0] if databases else "{{DATABASE}}"
    primary_test = test_frameworks[0] if test_frameworks else "{{TEST_FRAMEWORK}}"
    frontend_fw = frontend.get("frameworks", ["{{FRONTEND_FRAMEWORK}}"])[0] if isinstance(frontend, dict) else "{{FRONTEND_FRAMEWORK}}"
    styling = frontend.get("styling", ["{{STYLING}}"])[0] if isinstance(frontend, dict) and frontend.get("styling") else "{{STYLING}}"

    return {
        "{{LANGUAGE}}": primary_lang,
        "{{LANGUAGES}}": ", ".join(languages) if languages else "{{LANGUAGES}}",
        "{{FRAMEWORK}}": primary_framework,
        "{{WAREHOUSE}}": primary_db,
        "{{DATABASE}}": primary_db,
        "{{TARGET_SYSTEM}}": primary_db,
        "{{TEST_FRAMEWORK}}": primary_test,
        "{{LANGUAGE_AND_TEST_FRAMEWORK}}": f"{primary_lang}/{primary_test}" if primary_lang != "{{LANGUAGE}}" else "{{LANGUAGE_AND_TEST_FRAMEWORK}}",
        "{{FRONTEND_FRAMEWORK}}": frontend_fw,
        "{{STYLING}}": styling,
        "{{STYLING_APPROACH}}": styling,
        "{{CI_PLATFORM}}": infra.get("ci_tool", "{{CI_PLATFORM}}") if isinstance(infra, dict) else "{{CI_PLATFORM}}",
        "{{NAMING_CONVENTION}}": conventions.get("naming", "{{NAMING_CONVENTION}}") if isinstance(conventions, dict) else "{{NAMING_CONVENTION}}",
        "{{REPO_NAME}}": profile.get("project_name", "{{REPO_NAME}}"),
        "{{ARCHITECTURE}}": profile.get("architecture", "{{ARCHITECTURE}}"),
    }


def adapt_template(template_text: str, replacements: dict) -> str:
    """Replace placeholders in a template with project-specific values.
    Only replaces placeholders that have real values (not other placeholders)."""
    result = template_text
    for placeholder, value in replacements.items():
        if not value.startswith("{{"):  # Only replace if we have a real value
            result = result.replace(placeholder, value)
    return result


def adapt_file(template_path: Path, output_path: Path, replacements: dict):
    """Adapt a single template file."""
    content = template_path.read_text()
    adapted = adapt_template(content, replacements)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(adapted)
    print(f"  ✓ {template_path.name} → {output_path}")


def adapt_directory(template_dir: Path, output_dir: Path, replacements: dict):
    """Adapt all .md files in a directory."""
    for md_file in sorted(template_dir.glob("**/*.md")):
        relative = md_file.relative_to(template_dir)
        out = output_dir / relative
        adapt_file(md_file, out, replacements)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Adapt prompt templates to a project profile")
    parser.add_argument("--profile", required=True, help="Path to profile.yml from scan_codebase.py")
    parser.add_argument("--template", help="Single template file to adapt")
    parser.add_argument("--template-dir", help="Directory of templates to adapt")
    parser.add_argument("--output", help="Output file (for single template)")
    parser.add_argument("--output-dir", help="Output directory (for template dir)")

    args = parser.parse_args()

    # Load profile
    profile_text = Path(args.profile).read_text()
    profile = parse_simple_yaml(profile_text)
    replacements = build_replacements(profile)

    print(f"Project: {profile.get('project_name', 'unknown')}")
    print(f"Stack: {', '.join(profile.get('languages', []))}")
    print(f"Frameworks: {', '.join(profile.get('frameworks', []))}")
    print()

    if args.template and args.output:
        adapt_file(Path(args.template), Path(args.output), replacements)
    elif args.template_dir and args.output_dir:
        adapt_directory(Path(args.template_dir), Path(args.output_dir), replacements)
    else:
        print("Provide either --template + --output, or --template-dir + --output-dir")
        sys.exit(1)

    print("\nDone! Prompts adapted to your project.")
