#!/usr/bin/env python3
"""
Codebase Scanner for Prompt Engineering Toolkit

Scans a codebase and produces a structured project profile (YAML)
that the skill uses to adapt prompt templates.

Usage:
    python scan_codebase.py /path/to/repo [--output profile.yml]

The scanner is intentionally fast and non-invasive — it reads file
metadata, package manifests, and directory structure. It never executes
code or modifies anything.
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from collections import Counter

# ── Detection maps ──────────────────────────────────────────────────

LANGUAGE_EXTENSIONS = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
    ".tsx": "TypeScript (React)", ".jsx": "JavaScript (React)",
    ".go": "Go", ".rs": "Rust", ".java": "Java", ".kt": "Kotlin",
    ".rb": "Ruby", ".php": "PHP", ".cs": "C#", ".cpp": "C++",
    ".c": "C", ".swift": "Swift", ".scala": "Scala",
    ".r": "R", ".R": "R", ".sql": "SQL",
}

FRAMEWORK_FILES = {
    "package.json": "node",
    "requirements.txt": "python", "pyproject.toml": "python",
    "Pipfile": "python", "setup.py": "python", "setup.cfg": "python",
    "Cargo.toml": "rust", "go.mod": "go", "Gemfile": "ruby",
    "build.gradle": "java/kotlin", "pom.xml": "java",
    "composer.json": "php", "*.csproj": "dotnet",
}

FRAMEWORK_INDICATORS = {
    # Python frameworks
    "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
    "starlette": "Starlette", "tornado": "Tornado", "celery": "Celery",
    "airflow": "Apache Airflow", "prefect": "Prefect", "dagster": "Dagster",
    "dbt-core": "dbt", "dbt": "dbt",
    "pandas": "pandas", "polars": "polars", "pyspark": "PySpark",
    "sqlalchemy": "SQLAlchemy", "alembic": "Alembic",
    # JS/TS frameworks
    "react": "React", "next": "Next.js", "vue": "Vue",
    "nuxt": "Nuxt", "svelte": "Svelte", "angular": "Angular",
    "express": "Express", "fastify": "Fastify", "nestjs": "NestJS",
    "prisma": "Prisma", "drizzle-orm": "Drizzle",
    "tailwindcss": "Tailwind CSS",
    # Testing
    "pytest": "pytest", "jest": "Jest", "vitest": "Vitest",
    "mocha": "Mocha", "cypress": "Cypress", "playwright": "Playwright",
    "@testing-library/react": "React Testing Library",
    # Go
    "gin-gonic/gin": "Gin", "gorilla/mux": "Gorilla Mux",
    # Rust
    "actix-web": "Actix Web", "axum": "Axum", "tokio": "Tokio",
}

DATA_INDICATORS = {
    "snowflake-connector-python": "Snowflake",
    "snowflake-sqlalchemy": "Snowflake",
    "google-cloud-bigquery": "BigQuery",
    "bigquery": "BigQuery",
    "psycopg2": "PostgreSQL", "asyncpg": "PostgreSQL",
    "pymongo": "MongoDB", "motor": "MongoDB",
    "mysql-connector-python": "MySQL", "pymysql": "MySQL",
    "redis": "Redis", "sqlalchemy": "SQLAlchemy",
    "databricks": "Databricks",
}


def scan_directory_structure(repo_path: Path) -> dict:
    """Get a picture of how the repo is organized."""
    structure = {
        "top_level_dirs": [],
        "has_src": False,
        "has_tests": False,
        "has_docs": False,
        "has_ci": False,
        "has_docker": False,
        "has_k8s": False,
        "has_migrations": False,
        "has_frontend": False,
        "has_ai_config": False,
        "ai_config_dirs": [],
    }

    for item in sorted(repo_path.iterdir()):
        if item.name.startswith(".") and item.is_dir():
            name = item.name
            if name in (".claude", ".copilot", ".cursor", ".aider"):
                structure["has_ai_config"] = True
                structure["ai_config_dirs"].append(name)
            if name in (".github", ".gitlab-ci", ".circleci"):
                structure["has_ci"] = True
            continue
        if item.is_dir():
            structure["top_level_dirs"].append(item.name)

    dir_names = set(structure["top_level_dirs"])
    structure["has_src"] = bool(dir_names & {"src", "app", "lib", "pkg", "internal", "cmd"})
    structure["has_tests"] = bool(dir_names & {"test", "tests", "__tests__", "spec", "e2e"})
    structure["has_docs"] = bool(dir_names & {"docs", "doc", "documentation"})
    structure["has_docker"] = (repo_path / "Dockerfile").exists() or (repo_path / "docker-compose.yml").exists()
    structure["has_k8s"] = bool(dir_names & {"k8s", "kubernetes", "helm", "charts"})
    structure["has_migrations"] = bool(dir_names & {"migrations", "alembic", "migrate", "db"})
    structure["has_frontend"] = bool(dir_names & {"components", "pages", "views", "public", "static", "frontend"})

    # Check for CI files
    if (repo_path / ".github" / "workflows").exists():
        structure["ci_tool"] = "GitHub Actions"
    elif (repo_path / ".gitlab-ci.yml").exists():
        structure["ci_tool"] = "GitLab CI"
    elif (repo_path / "Jenkinsfile").exists():
        structure["ci_tool"] = "Jenkins"
    elif (repo_path / ".circleci").exists():
        structure["ci_tool"] = "CircleCI"

    github_copilot_dir = repo_path / ".github" / "copilot"
    if github_copilot_dir.exists():
        structure["has_ai_config"] = True
        structure["ai_config_dirs"].append(".github/copilot")

    return structure


def detect_languages(repo_path: Path) -> list:
    """Count file extensions to determine primary languages."""
    ext_count = Counter()
    for root, dirs, files in os.walk(repo_path):
        # Skip hidden dirs, node_modules, vendor, venv
        dirs[:] = [d for d in dirs if not d.startswith(".")
                    and d not in ("node_modules", "vendor", "venv", ".venv",
                                   "__pycache__", "dist", "build", "target")]
        for f in files:
            ext = Path(f).suffix
            if ext in LANGUAGE_EXTENSIONS:
                ext_count[ext] += 1

    # Sort by count, return top languages
    sorted_langs = sorted(ext_count.items(), key=lambda x: -x[1])
    result = []
    seen = set()
    for ext, count in sorted_langs[:5]:
        lang = LANGUAGE_EXTENSIONS[ext]
        base_lang = lang.split(" (")[0]  # "TypeScript (React)" -> "TypeScript"
        if base_lang not in seen and count >= 3:
            result.append({"language": lang, "file_count": count})
            seen.add(base_lang)
    return result


def parse_package_json(repo_path: Path) -> dict:
    """Parse package.json for Node.js projects."""
    pj = repo_path / "package.json"
    if not pj.exists():
        return {}
    try:
        data = json.loads(pj.read_text())
        deps = {}
        deps.update(data.get("dependencies", {}))
        deps.update(data.get("devDependencies", {}))
        return {
            "name": data.get("name", ""),
            "deps": deps,
            "scripts": list(data.get("scripts", {}).keys()),
        }
    except (json.JSONDecodeError, OSError):
        return {}


def parse_python_deps(repo_path: Path) -> list:
    """Parse Python dependency files."""
    deps = []
    # requirements.txt
    req = repo_path / "requirements.txt"
    if req.exists():
        try:
            for line in req.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("-"):
                    pkg = re.split(r"[>=<!\[]", line)[0].strip()
                    if pkg:
                        deps.append(pkg.lower())
        except OSError:
            pass

    # pyproject.toml — simple parse
    pyproject = repo_path / "pyproject.toml"
    if pyproject.exists():
        try:
            content = pyproject.read_text()
            # Find dependencies section
            in_deps = False
            for line in content.splitlines():
                if re.match(r"\[.*dependencies.*\]", line, re.IGNORECASE):
                    in_deps = True
                    continue
                if in_deps and line.startswith("["):
                    in_deps = False
                if in_deps:
                    m = re.match(r'^"?([a-zA-Z0-9_-]+)', line.strip())
                    if m:
                        deps.append(m.group(1).lower())
        except OSError:
            pass

    return list(set(deps))


def detect_frameworks(repo_path: Path) -> dict:
    """Detect frameworks and tools from dependencies."""
    result = {
        "frameworks": [],
        "testing": [],
        "data_tools": [],
        "databases": [],
    }

    all_deps = set()

    # Node.js deps
    pkg = parse_package_json(repo_path)
    if pkg:
        all_deps.update(pkg.get("deps", {}).keys())

    # Python deps
    py_deps = parse_python_deps(repo_path)
    all_deps.update(py_deps)

    # Go deps (go.mod)
    gomod = repo_path / "go.mod"
    if gomod.exists():
        try:
            for line in gomod.read_text().splitlines():
                parts = line.strip().split()
                if len(parts) >= 1 and "/" in parts[0]:
                    all_deps.add(parts[0].split("/")[-1])
        except OSError:
            pass

    # Match against indicators
    for dep in all_deps:
        dep_lower = dep.lower().replace("_", "-")
        for indicator, name in FRAMEWORK_INDICATORS.items():
            if indicator in dep_lower:
                # Categorize
                if name in ("pytest", "Jest", "Vitest", "Mocha", "Cypress",
                            "Playwright", "React Testing Library"):
                    if name not in result["testing"]:
                        result["testing"].append(name)
                elif name in ("Apache Airflow", "Prefect", "Dagster", "dbt",
                              "pandas", "polars", "PySpark"):
                    if name not in result["data_tools"]:
                        result["data_tools"].append(name)
                else:
                    if name not in result["frameworks"]:
                        result["frameworks"].append(name)

        for indicator, name in DATA_INDICATORS.items():
            if indicator in dep_lower:
                if name not in result["databases"]:
                    result["databases"].append(name)

    return result


def detect_architecture(repo_path: Path, structure: dict, frameworks: dict) -> str:
    """Infer the architecture pattern."""
    dirs = set(structure["top_level_dirs"])

    # Monorepo indicators
    if dirs & {"packages", "apps", "services", "modules"}:
        return "monorepo"
    if (repo_path / "lerna.json").exists():
        return "monorepo"
    if (repo_path / "nx.json").exists():
        return "monorepo"
    if (repo_path / "turbo.json").exists():
        return "monorepo"
    if (repo_path / "pnpm-workspace.yaml").exists():
        return "monorepo"

    # Microservices
    if len(dirs & {"services", "service", "api", "gateway"}) >= 2:
        return "microservices"

    # Serverless
    if (repo_path / "serverless.yml").exists():
        return "serverless"
    if dirs & {"lambda", "functions"}:
        return "serverless"

    # Library
    if dirs & {"src"} and not structure["has_frontend"]:
        fw = frameworks.get("frameworks", [])
        if not any(f in fw for f in ["React", "Vue", "Next.js", "Angular",
                                       "Express", "FastAPI", "Django", "Flask"]):
            return "library"

    return "monolith"


def detect_conventions(repo_path: Path, languages: list) -> dict:
    """Detect naming conventions and patterns."""
    conventions = {}

    primary = languages[0]["language"] if languages else ""
    if "Python" in primary:
        conventions["naming"] = "snake_case"
    elif primary in ("JavaScript", "TypeScript", "TypeScript (React)", "Java", "Kotlin"):
        conventions["naming"] = "camelCase"
    elif "Go" in primary:
        conventions["naming"] = "camelCase (exported: PascalCase)"
    elif "Rust" in primary:
        conventions["naming"] = "snake_case"

    # Check for linting config
    lint_configs = [
        (".eslintrc", "ESLint"), (".eslintrc.js", "ESLint"), (".eslintrc.json", "ESLint"),
        ("eslint.config.js", "ESLint"), ("eslint.config.mjs", "ESLint"),
        (".prettierrc", "Prettier"), (".prettierrc.json", "Prettier"),
        ("ruff.toml", "Ruff"), (".flake8", "Flake8"),
        (".editorconfig", "EditorConfig"),
        ("biome.json", "Biome"),
    ]
    linters = []
    for filename, name in lint_configs:
        if (repo_path / filename).exists():
            linters.append(name)
    conventions["linters"] = linters

    return conventions


def build_profile(repo_path: Path) -> dict:
    """Build the complete project profile."""
    repo_path = repo_path.resolve()

    structure = scan_directory_structure(repo_path)
    languages = detect_languages(repo_path)
    frameworks = detect_frameworks(repo_path)
    architecture = detect_architecture(repo_path, structure, frameworks)
    conventions = detect_conventions(repo_path, languages)
    frontend_frameworks = [
        f for f in frameworks["frameworks"]
        if f in ("React", "Vue", "Next.js", "Nuxt", "Svelte", "Angular")
    ]
    frontend_styling = [
        f for f in frameworks["frameworks"]
        if f in ("Tailwind CSS",)
    ]
    frontend_detected = structure["has_frontend"] or bool(frontend_frameworks)

    # Try to get project name
    pkg = parse_package_json(repo_path)
    name = pkg.get("name", "") if pkg else ""
    if not name:
        name = repo_path.name

    profile = {
        "project_name": name,
        "scanned_at": datetime.now().isoformat(),
        "languages": [l["language"] for l in languages],
        "language_details": languages,
        "frameworks": frameworks["frameworks"],
        "architecture": architecture,
        "databases": frameworks["databases"],
        "data_tools": frameworks["data_tools"],
        "testing": {
            "frameworks": frameworks["testing"],
            "has_tests": structure["has_tests"],
        },
        "infrastructure": {
            "has_docker": structure["has_docker"],
            "has_k8s": structure["has_k8s"],
            "ci_tool": structure.get("ci_tool", "none detected"),
        },
        "frontend": {
            "detected": frontend_detected,
            "frameworks": frontend_frameworks,
            "styling": frontend_styling,
        },
        "conventions": conventions,
        "structure": {
            "top_level_dirs": structure["top_level_dirs"],
            "has_docs": structure["has_docs"],
            "has_migrations": structure["has_migrations"],
        },
        "existing_ai_config": {
            "has_config": structure["has_ai_config"],
            "directories": structure["ai_config_dirs"],
        },
    }

    return profile


def to_yaml_string(data: dict, indent: int = 0) -> str:
    """Simple YAML serializer (no external deps needed)."""
    lines = []
    prefix = "  " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{prefix}{key}:")
            lines.append(to_yaml_string(value, indent + 1))
        elif isinstance(value, list):
            if not value:
                lines.append(f"{prefix}{key}: []")
            elif all(isinstance(v, str) for v in value):
                lines.append(f"{prefix}{key}: [{', '.join(value)}]")
            else:
                lines.append(f"{prefix}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        first = True
                        for k, v in item.items():
                            if first:
                                lines.append(f"{prefix}  - {k}: {v}")
                                first = False
                            else:
                                lines.append(f"{prefix}    {k}: {v}")
                    else:
                        lines.append(f"{prefix}  - {item}")
        elif isinstance(value, bool):
            lines.append(f"{prefix}{key}: {'true' if value else 'false'}")
        else:
            lines.append(f"{prefix}{key}: {value}")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_codebase.py /path/to/repo [--output profile.yml]")
        sys.exit(1)

    repo = Path(sys.argv[1])
    if not repo.is_dir():
        print(f"Error: {repo} is not a directory")
        sys.exit(1)

    output = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output = sys.argv[idx + 1]

    profile = build_profile(repo)
    yaml_str = to_yaml_string(profile)

    if output:
        Path(output).write_text(yaml_str)
        print(f"Profile written to {output}")
    else:
        print(yaml_str)
