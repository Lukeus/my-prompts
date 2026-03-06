---
name: prompt-eng-toolkit
description: |
  Self-adapting prompt toolkit with 40+ templates for data engineering, software dev, UI, prompt refinement, and codebase research. Scans a repo, detects the stack, and adapts all prompts automatically. Use whenever the user wants to: set up a prompt library in .claude/.copilot/.cursor/, scan a codebase and generate tailored prompts, get templates for pipelines/APIs/code review/debugging/testing/docs, create DeepWiki-style documentation, or bootstrap a team's prompt collection. Trigger on: "prompt library", "prompt templates", "adapt prompts", "set up prompts for this project", "customize prompts for my repo", or any request for systematic engineering prompts.
---

# Prompt Engineering Toolkit

A library of 40+ prompt templates and playbooks that adapt themselves to whatever codebase they live in. The core idea: instead of generic prompts, these prompts understand *your* stack, *your* conventions, and *your* architecture — because they were tuned by scanning your actual code.

## How It Works

There are two modes of operation:

### Mode 1: Scan & Adapt (Primary)

The user places this skill in their repo and asks you to adapt it. You scan the codebase, detect the stack, and rewrite the `{{PLACEHOLDER}}` values in every prompt template with real values from the project.

### Mode 2: On-Demand Generation

The user asks for a specific type of prompt (e.g., "give me a code review prompt for this project"). You read the relevant reference file, scan enough of the codebase to fill in context, and produce a tailored prompt.

---

## Scan & Adapt Workflow

When the user asks you to adapt prompts for their codebase, follow these steps:

### Step 1: Codebase Reconnaissance

Gather the fingerprint of the project. Run these checks (adapt based on what's available):

```
# What you're looking for and where to find it
1. Languages & frameworks  → package.json, requirements.txt, Cargo.toml, go.mod, Gemfile, *.csproj, build.gradle
2. Directory structure      → tree -L 3 (or ls -R with depth limit)
3. Architecture pattern     → Look for src/, app/, lib/, services/, components/, pages/, routes/
4. Database/data layer      → Look for migrations/, models/, schema/, prisma/, alembic/, dbt/
5. Testing setup            → Look for test/, __tests__/, spec/, *.test.*, pytest.ini, jest.config.*
6. CI/CD                    → .github/workflows/, .gitlab-ci.yml, Jenkinsfile, .circleci/
7. Containerization         → Dockerfile, docker-compose.yml, k8s/
8. Linting/formatting       → .eslintrc, .prettierrc, ruff.toml, .editorconfig, pyproject.toml
9. Existing AI config       → .claude/, .copilot/, .cursor/, .aider*, CLAUDE.md
10. README & docs           → README.md, docs/, CONTRIBUTING.md, ADRs
```

### Step 2: Build the Project Profile

From the reconnaissance, assemble a structured profile:

```yaml
project_name: <from package.json name, repo dir name, or README>
languages: [<primary>, <secondary>]
frameworks: [<web framework>, <test framework>, <ORM>, etc.]
architecture: <monolith | microservices | monorepo | serverless | library>
database: <postgres | mysql | mongo | snowflake | bigquery | none>
data_tools: [<dbt | airflow | spark | pandas | etc.>]
frontend: <react | vue | svelte | angular | none>
styling: <tailwind | css-modules | styled-components | plain-css>
testing:
  framework: <pytest | jest | go-test | etc.>
  patterns: <what testing conventions exist>
ci_cd: <github-actions | gitlab-ci | jenkins | etc.>
deployment: <docker | k8s | serverless | bare-metal>
conventions:
  naming: <camelCase | snake_case | etc.>
  error_handling: <pattern observed>
  directory_org: <how code is organized>
notable_patterns: [<anything distinctive — custom abstractions, unusual architecture, etc.>]
```

### Step 3: Select Relevant Prompt Categories

Not every project needs every prompt. Based on the profile, select which categories to generate:

| If the project has...             | Generate prompts from...                    |
|-----------------------------------|---------------------------------------------|
| A data layer (models, migrations) | `data-engineering/` templates               |
| dbt, Airflow, Spark              | `data-engineering/stack-specific/`           |
| Backend API routes                | `software-development/` (API, testing, errors) |
| Python code                       | `software-development/stack-specific/python` |
| Docker/CI config                  | `software-development/stack-specific/devops` |
| Frontend components               | `ui-development/` templates                 |
| React/Vue/Svelte                  | `ui-development/stack-specific/`            |
| Any code at all                   | `codebase-research/` (always useful)        |
| Using AI assistants               | `prompt-refinement/` templates              |

### Step 4: Adapt Each Prompt

For each selected prompt template, replace `{{PLACEHOLDER}}` values with project-specific defaults. The goal is that when a developer copies a prompt, 60-80% of the fields are already filled in — they only need to add the specifics of their current task.

**Adaptation rules:**
- `{{LANGUAGE}}` → the project's primary language
- `{{FRAMEWORK}}` → the detected framework
- `{{WAREHOUSE}}` → the detected database/warehouse
- `{{TEST_FRAMEWORK}}` → the detected test runner
- Stack-specific prompts get the actual tool versions and config patterns
- Playbook prompts get the project's architecture baked into the context sections
- Leave task-specific placeholders (like `{{YOUR_CODE}}` or `{{BUG_DESCRIPTION}}`) as-is — those change every use

**What "adapted" looks like:**

Before (generic):
```
**Language:** {{LANGUAGE}}
**Framework:** {{FRAMEWORK}}
**Test framework:** {{TEST_FRAMEWORK}}
```

After (adapted for a Next.js project):
```
**Language:** TypeScript
**Framework:** Next.js 14 (App Router)
**Test framework:** Jest + React Testing Library
```

### Step 5: Write to the Target Directory

Ask the user where they want the prompts. Common locations:

- `.claude/prompts/` — for Claude Code users
- `.github/copilot/prompts/` — for GitHub Copilot users
- `.cursor/prompts/` — for Cursor users
- `docs/prompts/` — for team-shared prompt libraries
- `.ai/prompts/` — generic, tool-agnostic location

Write an adapted version of each selected prompt, plus:
- `README.md` — overview and usage guide
- `INDEX.md` — master index linking to every prompt
- `_project-profile.yml` — the detected profile (so prompts can be re-adapted later)

### Step 6: Generate Rescan Instructions

At the top of the README, include instructions for re-adapting:

```markdown
## Keeping Prompts Updated

These prompts were auto-adapted to this codebase on {{DATE}}.
If your stack changes, ask your AI assistant:

> "Scan the codebase and re-adapt the prompts in {{PROMPT_DIR}}"

The assistant will re-run the scan, detect changes, and update
only the prompts that need it (preserving any manual edits you've made).
```

---

## Reference Files

The `references/` directory contains the full prompt templates organized by category. Read the relevant file when you need the raw templates:

- `references/data-engineering.md` — Pipeline design, data quality, schema design, SQL optimization, ETL debugging, dbt, Airflow, migration and modeling review playbooks
- `references/software-development.md` — Code review, API design, testing, refactoring, error handling, architecture and debugging playbooks, Python and DevOps prompts
- `references/ui-development.md` — Component design, layouts, forms, responsive audit, design system and accessibility playbooks, React prompts
- `references/prompt-refinement.md` — Prompt improver, system prompt generator, CoT designer, eval generator, engineering workflow and migration playbooks
- `references/codebase-research.md` — Repo onboarding, dependency mapping, pattern detection, impact analysis, wiki/API/README/diagram generators, monorepo and legacy analysis

**When to read which file:** Only read the references you need for the current task. If the user asks to adapt everything, read them all. If they just want a code review prompt, read `software-development.md` only.

---

## On-Demand Prompt Generation

When the user asks for a specific prompt (not a full scan), follow this lighter workflow:

1. Identify which category and template they need
2. Read the relevant reference file
3. Do a quick scan of just enough codebase context to fill in the stack details
4. Output the adapted prompt directly in the conversation (and optionally save to file)

---

## Prompt Anatomy

Every prompt in this toolkit follows a consistent structure that makes them effective across LLMs:

1. **Context block** — Pre-filled with project-specific values so the LLM knows the environment
2. **Task description** — What to do, written as clear instructions
3. **Output specification** — Exactly what deliverables to produce
4. **Quality gates** — What "good" looks like (edge cases, constraints)
5. **`[OPTIONAL]` sections** — Extra capabilities the user can toggle on

The `{{PLACEHOLDER}}` convention means "fill this in for your task." Pre-adapted values (from the scan) are written as plain text. This visual distinction helps developers immediately see what they still need to provide.

---

## Multi-Tool Compatibility

These prompts are designed to work with any AI coding assistant. The adaptation step writes them to the correct directory, but the prompts themselves are LLM-agnostic. Key compatibility notes:

- **Claude Code (`.claude/`)**: Prompts are available as project context. Claude can reference them directly.
- **GitHub Copilot (`.github/copilot/`)**: Prompts work as instruction files that Copilot Chat can use.
- **Cursor (`.cursor/`)**: Prompts integrate with Cursor's rules and context system.
- **Generic**: Any tool that reads markdown files from the project directory can use these.

When writing to a tool-specific directory, add a brief note at the top of the README explaining how prompts integrate with that specific tool.
