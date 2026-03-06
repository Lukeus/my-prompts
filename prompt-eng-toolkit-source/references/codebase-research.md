# Codebase Research Prompts Reference

## Table of Contents

1. [Exploration Prompts](#exploration-prompts)
   - [Repository Onboarding](#repository-onboarding)
   - [Dependency Mapping](#dependency-mapping)
   - [Pattern Detection](#pattern-detection)
   - [Impact Analysis](#impact-analysis)

2. [Documentation Prompts](#documentation-prompts)
   - [Auto Wiki Generator](#auto-wiki-generator-deepwiki-style)
   - [API Documentation Generator](#api-documentation-generator)
   - [README Generator](#readme-generator)
   - [Architecture Diagram Generator](#architecture-diagram-generator)

3. [Stack-Specific Prompts](#stack-specific-prompts)
   - [Monorepo Analysis](#monorepo-analysis-prompts)
   - [Legacy Code Analysis](#legacy-code-analysis-prompts)

---

## Exploration Prompts

### Repository Onboarding

> Quickly understand an unfamiliar codebase — architecture, patterns, and entry points.

#### Prompt

```
I've just joined a project and need to understand this codebase. Here's what I know:

**Repository:** {{REPO_NAME_OR_URL}}
**Language(s):** {{LANGUAGES}}
**What the project does (if known):** {{BRIEF_DESCRIPTION}}
**My role:** {{WHAT_I_NEED_TO_WORK_ON}}

Analyze the codebase and give me a onboarding guide:

1. **Architecture overview** — What's the high-level structure? (monolith, microservices, monorepo, etc.)
2. **Directory map** — What does each top-level directory contain and why?
3. **Entry points** — Where does execution start? (main files, route handlers, event listeners)
4. **Core abstractions** — What are the key classes/modules/patterns everything is built on?
5. **Data flow** — How does data move through the system? (request → processing → storage)
6. **Configuration** — Where are environment variables, feature flags, and settings managed?
7. **Dependencies** — What are the critical external dependencies and what do they do?
8. **Testing** — How do I run tests? What testing patterns are used?
9. **Build & deploy** — How do I build, run locally, and deploy?
10. **Gotchas** — Common pitfalls, known tech debt, or unintuitive patterns to watch for

Format as a guide I could hand to the next new team member.
```

#### Usage Notes

- Feed in the directory tree (`tree -L 3`), key config files, and README for best results
- If the repo is too large, focus on the area relevant to your role
- Follow up with `dependency-mapping.md` for deeper analysis

---

### Dependency Mapping

> Map internal and external dependencies to understand coupling and risk.

#### Prompt

```
Analyze the dependencies in this codebase:

**Package manifest:**
```
{{PACKAGE_JSON_OR_REQUIREMENTS_TXT_OR_CARGO_TOML}}
```

**Import statements from key modules (sample):**
```
{{SAMPLE_IMPORTS_FROM_5_10_KEY_FILES}}
```

Map dependencies in two categories:

**External dependencies:**
1. List every external package with:
   - What it does (one line)
   - Is it actively maintained? (last release date, open issues)
   - Are there known security vulnerabilities?
   - How deeply coupled is the codebase to it? (easy to replace vs. fundamental)
   - License compatibility
2. Flag dependencies that are:
   - Abandoned (no updates in 12+ months)
   - Have overlapping functionality (two libraries doing the same thing)
   - Pinned to old major versions
   - Unusually large for what they do

**Internal dependencies:**
1. Which modules depend on which? (produce a dependency graph)
2. Identify circular dependencies
3. Find "god modules" that everything depends on
4. Find orphan modules nothing imports
5. Rate the coupling: tight (hard to change independently) vs. loose

Output a mermaid dependency diagram for the top 15 most-connected modules.
```

#### Usage Notes

- For large projects, focus on one service or package at a time
- The "deeply coupled" assessment helps prioritize migration efforts
- Circular dependencies are almost always a design smell — flag them

---

### Pattern Detection

> Identify design patterns, anti-patterns, and conventions used in a codebase.

#### Prompt

```
Analyze these code samples from {{REPO_NAME}} and identify the patterns in use:

```{{LANGUAGE}}
{{CODE_SAMPLES_FROM_MULTIPLE_FILES}}
```

Detect and catalog:

**Design patterns:**
- Which GoF or other named patterns are used? (Factory, Observer, Strategy, Repository, etc.)
- Are they implemented correctly or are there deviations?
- Are patterns consistent across the codebase or mixed?

**Architectural patterns:**
- MVC, MVVM, Clean Architecture, Hexagonal, CQRS, Event Sourcing?
- How strictly is the pattern followed?
- Where does the codebase deviate from the pattern?

**Conventions:**
- Naming conventions (variables, functions, files, directories)
- Error handling pattern
- Logging pattern
- Configuration management pattern
- Testing patterns (arrange-act-assert, given-when-then, test doubles approach)

**Anti-patterns detected:**
- God objects/classes
- Spaghetti code / unclear control flow
- Premature abstraction or over-engineering
- Copy-paste code (DRY violations)
- Magic numbers or hardcoded values
- Dead code

For each finding, provide:
- Example from the code
- Whether it's used consistently
- Recommendation (keep, refactor, or replace — and why)
```

#### Usage Notes

- Feed in 5-10 representative files for pattern detection
- Include test files — testing patterns reveal a lot about code quality
- The "conventions" section is gold for new team members

---

### Impact Analysis

> Before making a change, understand what it will affect.

#### Prompt

```
I need to make the following change to {{REPO_NAME}}:

**Change description:** {{WHAT_I_WANT_TO_CHANGE}}
**Files I plan to modify:**
- {{FILE_1}}: {{WHAT_CHANGES}}
- {{FILE_2}}: {{WHAT_CHANGES}}

**Relevant code context:**
```{{LANGUAGE}}
{{CODE_BEING_CHANGED_AND_ITS_CALLERS}}
```

Analyze the impact:

1. **Direct dependents** — What files/modules directly import or call the changed code?
2. **Transitive dependents** — What depends on the direct dependents? (2 levels deep)
3. **API/contract changes** — Does this change any public interfaces, API responses, or database schemas?
4. **Behavioral changes** — Will existing consumers see different behavior? List each change.
5. **Test impact** — Which tests will need updating? Which tests should be added?
6. **Configuration impact** — Are there environment variables, feature flags, or configs that need updating?
7. **Migration needs** — Is a data migration, API version bump, or deployment coordination needed?
8. **Risk assessment:**
   - Probability of breaking something: {{LOW | MEDIUM | HIGH}}
   - Blast radius if it breaks: {{SMALL | MEDIUM | LARGE}}
   - Recommended deployment strategy: {{DIRECT | FEATURE_FLAG | CANARY | BLUE_GREEN}}

Produce a checklist I can use before merging the PR.
```

#### Usage Notes

- Include callers and dependents in the code context — not just the code being changed
- The "transitive dependents" question catches non-obvious breakage
- The deployment strategy recommendation is especially valuable for high-risk changes

---

## Documentation Prompts

### Auto Wiki Generator (DeepWiki-Style)

> Generate comprehensive wiki-style documentation from a codebase, similar to DeepWiki.

#### Prompt — Full Wiki Generation

```
Generate a comprehensive wiki for this codebase:

**Repository:** {{REPO_NAME}}
**Language(s):** {{LANGUAGES}}
**Directory structure:**
```
{{TREE_OUTPUT}}
```

**Key source files:**
```{{LANGUAGE}}
{{PASTE_KEY_FILES_OR_SUMMARIES}}
```

Generate a wiki with these sections:

## 1. Project Overview
- What the project does (inferred from code, README, comments)
- Key features and capabilities
- Target users / use cases

## 2. Architecture
- System architecture diagram (mermaid)
- Component breakdown with responsibilities
- Data flow diagrams for core use cases
- Technology stack and why each piece was chosen (inferred)

## 3. Module Reference
For each major module/package:
- Purpose and responsibility
- Public API / exports
- Dependencies (what it imports)
- Key classes/functions with brief descriptions
- Configuration it reads

## 4. Data Model
- Entity relationship diagram (mermaid)
- Table/collection descriptions
- Key relationships and constraints
- Data flow from input to storage

## 5. API Reference (if applicable)
- All endpoints with methods, params, and response shapes
- Authentication requirements
- Rate limits and pagination
- Error response format

## 6. Configuration Guide
- All environment variables with descriptions and defaults
- Feature flags
- Configuration files and their schema

## 7. Development Guide
- Local setup instructions
- How to run tests
- How to add a new feature (following existing patterns)
- Coding conventions and style guide (inferred from code)

## 8. Glossary
- Domain-specific terms used in the codebase
- Abbreviations and acronyms

Format each section with clear headings, code examples from the actual codebase, and cross-references between sections.
```

#### Usage Notes

- For large repos, generate the wiki module-by-module rather than all at once
- Feed in the most important 10-15 files plus the directory tree
- The "inferred" sections are the most valuable — they extract undocumented knowledge
- Update the wiki whenever the architecture changes significantly

---

### API Documentation Generator

> Generate complete API documentation from source code.

#### Prompt

```
Generate API documentation from the following route/endpoint definitions:

**Framework:** {{FRAMEWORK}} (e.g., Express, FastAPI, Django, Spring Boot, Go Chi)
**Auth mechanism:** {{AUTH_TYPE}}

**Route code:**
```{{LANGUAGE}}
{{YOUR_ROUTE_HANDLERS}}
```

**Models/schemas used:**
```{{LANGUAGE}}
{{YOUR_DATA_MODELS}}
```

For each endpoint, document:

1. **Method & Path** — `GET /api/v1/users/{id}`
2. **Description** — What it does in one sentence
3. **Authentication** — Required? What role/scope?
4. **Path parameters** — Name, type, description, example
5. **Query parameters** — Name, type, required?, default, description
6. **Request body** — JSON schema with field descriptions and example
7. **Response** — Status codes with response body schema and example
8. **Error responses** — Each error status code with when it occurs
9. **Example request** — curl command
10. **Rate limiting** — If applicable

Output formats:
- Markdown (human-readable)
- OpenAPI 3.0 YAML snippet (machine-readable)

[OPTIONAL: Include SDK usage examples for {{LANGUAGE}}]
```

#### Usage Notes

- Include the data models — they're essential for request/response schemas
- The curl examples make the docs immediately testable
- For GraphQL, adapt the template to document queries, mutations, and subscriptions

---

### README Generator

> Create a professional README from codebase analysis.

#### Prompt

```
Generate a README.md for this project:

**Project files to analyze:**
- Directory tree: {{TREE_OUTPUT}}
- Package manifest: {{PACKAGE_JSON_OR_EQUIVALENT}}
- Existing README (if any): {{CURRENT_README}}
- CI config: {{CI_YAML}}
- Dockerfile (if any): {{DOCKERFILE}}

**Additional context:**
- Project purpose: {{BRIEF_DESCRIPTION}}
- Target audience: {{WHO_USES_THIS}} (developers, end users, both)
- License: {{LICENSE_TYPE}}

Generate a README with these sections:

1. **Title & badges** — Project name, build status, version, license badges
2. **One-liner** — What this project does in one compelling sentence
3. **Features** — Key capabilities as a brief list
4. **Quick start** — Get from zero to running in under 5 commands
5. **Installation** — Detailed setup for all supported platforms
6. **Usage** — Common use cases with code examples
7. **Configuration** — Environment variables and config options table
8. **API reference** — Brief overview (link to full docs if they exist)
9. **Development** — How to set up for development, run tests, contribute
10. **Architecture** — Brief overview with link to detailed docs
11. **Troubleshooting** — Common issues and solutions
12. **Contributing** — How to contribute, coding standards, PR process
13. **License** — License information

Style guidelines:
- Concise — each section should be scannable in 10 seconds
- Code examples should be copy-pasteable
- Use collapsible sections (<details>) for lengthy content
- Include both quickstart and detailed setup for different readers
```

#### Usage Notes

- The package manifest is the most information-dense input — always include it
- CI config reveals the build/test process better than most documentation
- If the project has multiple packages/services, generate a root README that links to sub-READMEs

---

### Architecture Diagram Generator

> Generate visual architecture diagrams from code analysis.

#### Prompt

```
Generate architecture diagrams for this codebase:

**Repository structure:**
```
{{TREE_OUTPUT}}
```

**Key configuration files:**
```
{{DOCKER_COMPOSE_OR_K8S_MANIFESTS_OR_INFRA_CONFIG}}
```

**Import/dependency graph (sample):**
```
{{IMPORTS_FROM_KEY_FILES}}
```

Generate the following diagrams in Mermaid syntax:

### 1. System Context Diagram (C4 Level 1)
- The system as a box
- All external actors (users, external services, third-party APIs)
- Relationships between them

### 2. Container Diagram (C4 Level 2)
- Each deployable unit (web app, API, database, queue, cache)
- Technology choices labeled
- Communication protocols between containers

### 3. Component Diagram (C4 Level 3)
- Major components within the primary service
- Their responsibilities and interactions
- Data stores they use

### 4. Data Flow Diagram
- For the top 3 most important use cases:
  - Step-by-step data flow from user action to response
  - Which components are involved at each step
  - Where data is transformed or persisted

### 5. Deployment Diagram
- Infrastructure layout (inferred from config files)
- Environments (dev, staging, prod)
- Networking boundaries

For each diagram:
- Use clear, descriptive labels
- Color-code by type (service=blue, database=green, external=gray)
- Add a brief text description explaining the diagram
```

#### Usage Notes

- Docker Compose files are the single best input for container diagrams
- Kubernetes manifests reveal the deployment architecture
- If you don't have infra config, the code's import graph still enables component diagrams
- C4 model levels provide a natural zoom hierarchy — start at Level 1

---

## Stack-Specific Prompts

### Monorepo Analysis Prompts

> Specialized prompts for understanding and navigating monorepo codebases.

---

#### Monorepo Map

```
Analyze this monorepo structure and create a navigation guide:

**Monorepo tool:** {{Nx | Turborepo | Lerna | Bazel | Rush | pnpm workspaces}}
**Root workspace config:**
```
{{WORKSPACE_CONFIG}}
```

**Directory tree (top 3 levels):**
```
{{TREE_OUTPUT}}
```

Produce:
1. **Package inventory** — Every package/app with its purpose, type (app, library, tool), and status (active, deprecated, experimental)
2. **Dependency graph** — Which packages depend on which (mermaid diagram)
3. **Build order** — What order must packages build in? What can build in parallel?
4. **Shared code map** — What's in shared libraries and who consumes them?
5. **Ownership map** — Infer team ownership from directory structure, CODEOWNERS, and commit patterns
6. **Hot spots** — Packages that change most frequently or have the most dependents (highest risk)
7. **Quick reference** — For a developer working on {{SPECIFIC_AREA}}, which packages matter and which can be ignored?
```

---

#### Cross-Package Change Analysis

```
I need to make a change that spans multiple packages in this monorepo:

**Change:** {{DESCRIPTION}}
**Primary package:** {{PACKAGE}}
**Monorepo tool:** {{TOOL}}

Help me:
1. Identify all packages affected by this change (direct and transitive)
2. Determine the correct order to make changes
3. Identify which tests to run (affected packages only, not the full suite)
4. Draft a PR strategy — single PR or multiple coordinated PRs?
5. Check for version bump needs (if packages are independently versioned)
6. List CI/CD pipelines that will trigger
```

#### Usage Notes

- Workspace config files (package.json workspaces, pnpm-workspace.yaml, nx.json) are essential input
- The dependency graph is the most valuable output — pin it somewhere visible
- For Nx repos, `nx graph` output can be fed directly into these prompts

---

### Legacy Code Analysis Prompts

> Specialized prompts for understanding and safely modifying legacy codebases.

---

#### Legacy Code Archaeology

```
I'm working with a legacy codebase that has limited documentation. Help me understand it:

**Language:** {{LANGUAGE}}
**Approximate age:** {{YEARS}}
**Original framework/version:** {{IF_KNOWN}}
**What this system does:** {{BUSINESS_PURPOSE}}

**Sample code (representative section):**
```{{LANGUAGE}}
{{CODE_SAMPLE}}
```

Analyze:
1. **Historical context** — What era of {{LANGUAGE}} development does this code reflect? What conventions were common then?
2. **Implicit patterns** — What design patterns are being used, even if named/implemented differently than modern versions?
3. **Hidden business logic** — What business rules are embedded in the code? (Often the most valuable undocumented knowledge)
4. **Technical debt inventory** — Categorize the debt:
   - Intentional (shortcuts that were known tradeoffs)
   - Accidental (code that drifted from its original design)
   - Environmental (outdated patterns that were best practice at the time)
5. **Risk map** — Which parts are most fragile? Where would a change most likely break things?
6. **Modernization priority** — If you could only modernize 3 things, what would have the biggest impact?
```

---

#### Safe Modification Guide

```
I need to modify this legacy code but I'm afraid of breaking things:

**Code to modify:**
```{{LANGUAGE}}
{{LEGACY_CODE}}
```

**Change needed:** {{WHAT_I_NEED_TO_DO}}
**Test coverage:** {{NONE | MINIMAL | MODERATE | GOOD}}
**Can I add tests?** {{YES | NO_BECAUSE}}

Help me make this change safely:
1. **Characterization tests** — If no tests exist, what tests should I write first to capture current behavior (even if the behavior is "wrong")?
2. **Seams** — Where can I insert a change without modifying existing code? (dependency injection points, interfaces, configuration)
3. **Strangler fig approach** — Can I wrap the old code and gradually redirect?
4. **Minimal change** — What's the smallest possible modification to achieve the goal?
5. **Rollback plan** — If the change causes issues, how do I revert safely?
6. **Verification** — How do I confirm the change works without comprehensive tests?
```

#### Usage Notes

- "Hidden business logic" findings should be documented immediately — this knowledge is perishable
- Characterization tests are the key to safely modifying legacy code
- The strangler fig pattern avoids big-bang rewrites — prefer it when possible
- Respect the legacy code — it's running in production for a reason
