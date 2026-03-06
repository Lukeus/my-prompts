# Prompt Library — Master Index

**41 prompts** across 5 categories. Templates for quick use, playbooks for depth, stack-specific variants for your tools.

---

## Data Engineering (9 prompts)

### Templates
- [Pipeline Design](data-engineering/templates/pipeline-design.md) — Design a data pipeline from source to destination
- [Data Quality Checks](data-engineering/templates/data-quality-checks.md) — Generate validation checks for a table
- [Schema Design](data-engineering/templates/schema-design.md) — Design a data model for a domain
- [ETL Debugging](data-engineering/templates/etl-debugging.md) — Diagnose a failing pipeline
- [SQL Optimization](data-engineering/templates/sql-optimization.md) — Speed up a slow query

### Playbooks
- [Migration Playbook](data-engineering/playbooks/migration-playbook.md) — End-to-end data migration (4 phases)
- [Data Modeling Review](data-engineering/playbooks/data-modeling-review.md) — Audit an existing data model (4 steps)

### Stack-Specific
- [dbt](data-engineering/stack-specific/dbt.md) — Models, tests, incremental debugging, macros, project structure
- [Airflow](data-engineering/stack-specific/airflow-orchestration.md) — DAG design, debugging, dynamic generation

---

## Software Development (9 prompts)

### Templates
- [Code Review](software-development/templates/code-review.md) — Thorough code review with severity levels
- [API Design](software-development/templates/api-design.md) — Design REST/GraphQL/gRPC APIs
- [Testing Strategy](software-development/templates/testing-strategy.md) — Generate unit and integration tests
- [Refactoring](software-development/templates/refactoring.md) — Improve code structure safely
- [Error Handling](software-development/templates/error-handling.md) — Design error handling for a system

### Playbooks
- [Architecture Design](software-development/playbooks/architecture-design.md) — From requirements to implementation plan (4 steps)
- [Debugging Playbook](software-development/playbooks/debugging-playbook.md) — Systematic bug diagnosis (3 steps)

### Stack-Specific
- [Python](software-development/stack-specific/python.md) — Scaffolding, type annotations, async, profiling
- [Docker & DevOps](software-development/stack-specific/docker-devops.md) — Dockerfiles, CI/CD, infrastructure as code

---

## UI Development (7 prompts)

### Templates
- [Component Design](ui-development/templates/component-design.md) — Build a reusable UI component
- [Layout from Description](ui-development/templates/layout-from-description.md) — Generate a page layout from natural language
- [Form Builder](ui-development/templates/form-builder.md) — Complete form with validation and a11y
- [Responsive Audit](ui-development/templates/responsive-audit.md) — Audit UI for responsive design issues

### Playbooks
- [Design System](ui-development/playbooks/design-system-playbook.md) — Build a component library from scratch (4 steps)
- [Accessibility Audit](ui-development/playbooks/accessibility-audit.md) — Comprehensive a11y review (3 steps)

### Stack-Specific
- [React](ui-development/stack-specific/react.md) - Hooks, state management, performance, class-to-hooks migration

---

## Prompt Refinement (6 prompts)

### Templates
- [Prompt Improver](prompt-refinement/templates/prompt-improver.md) — Upgrade a rough prompt to production quality
- [System Prompt Generator](prompt-refinement/templates/system-prompt-generator.md) — Create a system prompt for an AI role
- [Chain-of-Thought Designer](prompt-refinement/templates/chain-of-thought-designer.md) — Build structured reasoning prompts
- [Eval Generator](prompt-refinement/templates/eval-generator.md) — Create test cases to measure prompt quality

### Playbooks
- [Prompt Engineering Workflow](prompt-refinement/playbooks/prompt-engineering-workflow.md) — Requirements -> draft -> test -> production (4 phases)
- [Prompt Migration](prompt-refinement/playbooks/prompt-migration.md) — Migrate prompts between models (3 steps)

---

## Codebase Research (10 prompts)

### Exploration
- [Repo Onboarding](codebase-research/exploration/repo-onboarding.md) — Understand an unfamiliar codebase fast
- [Dependency Mapping](codebase-research/exploration/dependency-mapping.md) — Map internal and external dependencies
- [Pattern Detection](codebase-research/exploration/pattern-detection.md) — Identify design patterns and anti-patterns
- [Impact Analysis](codebase-research/exploration/impact-analysis.md) — Understand what a change will affect

### Documentation Generation
- [Auto Wiki Generator](codebase-research/documentation/auto-wiki-generator.md) — DeepWiki-style comprehensive docs from code
- [API Docs Generator](codebase-research/documentation/api-docs-generator.md) — Generate API reference from source
- [README Generator](codebase-research/documentation/readme-generator.md) — Professional README from codebase analysis
- [Architecture Diagram Generator](codebase-research/documentation/architecture-diagram-generator.md) — C4 model diagrams from code

### Stack-Specific
- [Monorepo Analysis](codebase-research/stack-specific/monorepo-analysis.md) — Navigate and understand monorepo structures
- [Legacy Code Analysis](codebase-research/stack-specific/legacy-code-analysis.md) — Safely understand and modify legacy code
