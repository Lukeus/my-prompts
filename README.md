# Prompts

A collection of 41 prompt templates, playbooks, and a self-adapting toolkit that tailors prompts to your codebase.

## What's Inside

### prompt-library/

Ready-to-use prompt templates and playbooks across five engineering domains:

| Category | Prompts | Includes |
|----------|---------|----------|
| **Data Engineering** | 9 | Pipeline design, data quality, schema design, SQL optimization, ETL debugging, dbt, Airflow |
| **Software Development** | 9 | Code review, API design, testing, refactoring, error handling, Python, Docker/DevOps |
| **UI Development** | 7 | Component design, layouts, forms, responsive audit, design systems, accessibility, React |
| **Prompt Refinement** | 6 | Prompt improver, system prompt generator, chain-of-thought, evals, migration |
| **Codebase Research** | 10 | Repo onboarding, dependency mapping, pattern detection, impact analysis, doc generation, monorepo/legacy analysis |

Each category is organized into **templates** (quick fill-and-go), **playbooks** (multi-step workflows), and **stack-specific** variants.

See [prompt-library/INDEX.md](prompt-library/INDEX.md) for the full list with descriptions.

### prompt-eng-toolkit-source/

The adaptation engine. Scans a codebase, detects the stack (languages, frameworks, databases, CI/CD, testing), and rewrites `{{PLACEHOLDER}}` values in every prompt template with real values from your project.

## Repository Structure

```
prompts/
├── prompt-library/           # 41 prompt templates and playbooks
│   ├── data-engineering/
│   ├── software-development/
│   ├── ui-development/
│   ├── prompt-refinement/
│   ├── codebase-research/
│   └── INDEX.md              # Master index of all prompts
├── prompt-eng-toolkit-source/ # Toolkit skill source
│   ├── references/           # Full template source files by category
│   ├── scripts/              # Codebase scanner and prompt adapter
│   ├── assets/               # Setup template
│   └── evals/                # Skill evaluation tests
└── prompt-eng-toolkit.skill  # Compiled skill file
```

## Quick Start

### Browse prompts directly

Open any template in [prompt-library/](prompt-library/), replace `{{PLACEHOLDER}}` values with your context, and paste into your AI assistant.

### Adapt prompts to a project

Use the toolkit to scan your codebase and generate project-specific prompts:

1. Point the toolkit at your repo
2. It detects your stack (languages, frameworks, database, testing, CI/CD)
3. All prompts get rewritten with your project's actual values
4. Output goes to `.claude/`, `.cursor/`, `.github/copilot/`, or wherever you prefer

The adapted prompts work with any AI coding assistant -- Claude, Copilot, Cursor, or anything that reads markdown.
