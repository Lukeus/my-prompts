# Software Development Prompts Reference

## Table of Contents

1. [Code Review Template](#code-review-template)
2. [API Design Template](#api-design-template)
3. [Testing Strategy Template](#testing-strategy-template)
4. [Refactoring Template](#refactoring-template)
5. [Error Handling Design Template](#error-handling-design-template)
6. [Architecture Design Playbook](#architecture-design-playbook)
7. [Systematic Debugging Playbook](#systematic-debugging-playbook)
8. [Python-Specific Prompts](#python-specific-prompts)
9. [Docker & DevOps Prompts](#docker--devops-prompts)

---

## Code Review Template

> Get a thorough code review with actionable feedback.

### Prompt

```
Review the following code for quality, correctness, and maintainability:

**Language:** {{LANGUAGE}}
**Context:** {{WHAT_THIS_CODE_DOES}}
**PR/change description:** {{WHAT_CHANGED_AND_WHY}}

```{{LANGUAGE}}
{{YOUR_CODE}}
```

Review for:
1. **Correctness** — Bugs, edge cases, off-by-one errors, race conditions
2. **Security** — Injection, auth issues, secret handling, input validation
3. **Performance** — N+1 queries, unnecessary allocations, algorithmic complexity
4. **Readability** — Naming, structure, comments (too many or too few)
5. **Maintainability** — DRY violations, tight coupling, missing abstractions
6. **Testing** — Is this testable? What tests are missing?

Format feedback as:
- 🔴 **Must fix** — Bugs or security issues
- 🟡 **Should fix** — Performance or maintainability concerns
- 🟢 **Suggestion** — Style or minor improvements
- ✅ **Good** — Things done well (important for learning)
```

### Usage Notes

- Include surrounding context (imports, related functions) for better reviews
- Specify your team's conventions if they differ from language defaults
- Works best with functions/classes under ~200 lines — split large reviews

---

## API Design Template

> Design a REST or GraphQL API for a feature or service.

### Prompt

```
Design an API for the following feature:

**Feature:** {{FEATURE_DESCRIPTION}}
**API style:** {{REST | GraphQL | gRPC}}
**Authentication:** {{JWT | API key | OAuth2 | session}}
**Consumers:** {{WHO_WILL_CALL_THIS}} (e.g., web frontend, mobile app, internal service)

**Core entities:**
- {{ENTITY_1}}: {{BRIEF_DESCRIPTION}}
- {{ENTITY_2}}: {{BRIEF_DESCRIPTION}}

**Key operations:**
- {{OPERATION_1}}
- {{OPERATION_2}}
- {{OPERATION_3}}

Provide:
1. Endpoint/schema definitions with request/response shapes
2. HTTP methods, status codes, and error response format
3. Pagination strategy for list endpoints
4. Rate limiting recommendations
5. Versioning strategy
6. Example curl commands or queries for each endpoint
7. OpenAPI spec snippet (for REST) or schema definition (for GraphQL)

[OPTIONAL: Must support {{SPECIAL_REQUIREMENT}} such as webhooks, file uploads, or real-time subscriptions]
```

### Usage Notes

- Be specific about consumers — mobile APIs need different pagination than internal services
- Include error response format upfront to avoid inconsistency later
- Pair with `testing-strategy.md` to generate integration tests for the API

---

## Testing Strategy Template

> Generate a comprehensive test plan and test code for a feature.

### Prompt

```
Write tests for the following code/feature:

**Language/framework:** {{LANGUAGE_AND_TEST_FRAMEWORK}} (e.g., Python/pytest, TypeScript/Jest, Go/testing)
**Code under test:**
```{{LANGUAGE}}
{{YOUR_CODE_OR_FUNCTION_SIGNATURES}}
```
**What this does:** {{BRIEF_DESCRIPTION}}

Generate:
1. **Unit tests** — Cover happy path, edge cases, and error conditions
2. **Integration tests** — Test interactions with dependencies (DB, APIs, filesystem)
3. **Test fixtures/factories** — Reusable test data setup
4. **Mock definitions** — For external dependencies

For each test, include:
- Descriptive test name following "should_X_when_Y" or "test_X_given_Y" convention
- Arrange / Act / Assert structure
- Comments explaining why edge cases matter

Edge cases to always consider:
- Empty inputs, null/undefined values
- Boundary values (0, -1, MAX_INT, empty string)
- Concurrent access (if applicable)
- Unicode and special characters in string inputs
- Timezone-sensitive date operations
```

### Usage Notes

- Provide the function signatures at minimum — full implementation gives better tests
- Specify your mocking library preference (e.g., unittest.mock, sinon, testify/mock)
- Add `[OPTIONAL: Generate property-based tests using {{LIBRARY}}]` for thorough coverage

---

## Refactoring Template

> Refactor code to improve structure without changing behavior.

### Prompt

```
Refactor the following code to improve {{GOAL}}:

**Goal:** {{readability | performance | testability | modularity | all of the above}}
**Language:** {{LANGUAGE}}
**Constraints:** {{ANY_CONSTRAINTS}} (e.g., can't change public API, must stay backward compatible)

```{{LANGUAGE}}
{{YOUR_CODE}}
```

Provide:
1. Refactored code with clear comments on what changed and why
2. List of refactoring techniques applied (e.g., Extract Method, Replace Conditional with Polymorphism)
3. Before/after comparison of key metrics (cyclomatic complexity, line count, dependency count)
4. Any tests that should be added or updated
5. Migration steps if the refactoring should be done incrementally

Do NOT change the external behavior. If you spot bugs, note them separately but don't mix bug fixes with refactoring.
```

### Usage Notes

- "Don't mix bug fixes with refactoring" keeps changes reviewable
- For large refactors, ask for an incremental plan rather than a single big change
- Specify backward compatibility constraints to avoid breaking consumers

---

## Error Handling Design Template

> Design a consistent error handling strategy for an application or service.

### Prompt

```
Design an error handling strategy for the following system:

**Application type:** {{TYPE}} (e.g., REST API, CLI tool, background worker, web app)
**Language:** {{LANGUAGE}}
**Current approach:** {{HOW_ERRORS_ARE_HANDLED_NOW}} (or "none — starting fresh")

Provide:
1. Error classification taxonomy (e.g., validation, auth, not found, internal, external dependency)
2. Custom error/exception class hierarchy
3. Error response format (for APIs) or error display approach (for UIs)
4. Logging strategy — what to log at each level (error, warn, info)
5. Retry and circuit breaker patterns for recoverable errors
6. Error code catalog with human-readable messages
7. How to propagate errors across service boundaries

Implementation requirements:
- Errors should be actionable — tell the caller what to do
- Internal details (stack traces, SQL) must never leak to clients
- Errors should be easy to search in logs (structured logging format)
- Include correlation IDs for tracing errors across services
```

### Usage Notes

- This is a foundational prompt — run it early in a project
- The error code catalog becomes a reference for your whole team
- Pair with monitoring/alerting setup for production readiness

---

## Architecture Design Playbook

> Multi-step workflow for designing a system from requirements to implementation plan.

### When to Use

- Starting a new service or major feature
- Evaluating whether to build vs. buy
- Preparing for a technical design review
- Scaling an existing system that's hitting limits

---

### Step 1: Requirements Clarification

```
I'm designing a system for {{HIGH_LEVEL_DESCRIPTION}}.

Here's what I know:
- **Users:** {{WHO_AND_HOW_MANY}}
- **Core use cases:** {{LIST_MAIN_USER_FLOWS}}
- **Scale:** {{REQUESTS_PER_SECOND | STORAGE_NEEDS | CONCURRENT_USERS}}
- **Latency requirements:** {{P50_AND_P99_TARGETS}}
- **Availability target:** {{UPTIME_SLA}}
- **Budget constraints:** {{IF_ANY}}

Before I design, help me identify:
1. Ambiguous requirements that need clarification
2. Implicit requirements I might be missing (security, compliance, observability)
3. Scale-related requirements I should plan for (10x growth)
4. Non-functional requirements that are easy to forget
5. Questions I should ask stakeholders before proceeding
```

---

### Step 2: Architecture Options

```
Given these requirements for {{SYSTEM_NAME}}:

{{PASTE_REQUIREMENTS_FROM_STEP_1}}

Propose 2-3 architecture options:

For each option, provide:
1. High-level architecture diagram (mermaid)
2. Key technology choices and why
3. How it handles the top 3 use cases
4. Scaling strategy
5. Failure modes and how they're mitigated
6. Estimated development effort
7. Operational complexity (how hard is this to run?)
8. Cost estimate at current and 10x scale

Then recommend one option with clear justification.
```

---

### Step 3: Detailed Design

```
I've chosen {{SELECTED_ARCHITECTURE}} for {{SYSTEM_NAME}}.

Now produce a detailed design:

1. **Component diagram** — All services, databases, queues, caches with their interactions
2. **Data model** — Core entities, relationships, storage decisions
3. **API contracts** — Key interfaces between components
4. **Data flow** — How a request flows through the system for each core use case
5. **Security design** — Auth, encryption, secrets management, network boundaries
6. **Observability** — Metrics, logs, traces, dashboards, alerts
7. **Deployment** — Infrastructure, CI/CD, environments, rollback strategy

For each component, note:
- Build vs. buy decision
- Technology choice with rationale
- Configuration that needs to be environment-specific
```

---

### Step 4: Implementation Plan

```
Given this architecture for {{SYSTEM_NAME}}:

{{SUMMARY_OF_DESIGN}}

Create a phased implementation plan:

Phase 1 (MVP): What's the minimum to ship something useful?
Phase 2: What adds the most value after MVP?
Phase 3: What completes the full vision?

For each phase:
1. Specific deliverables
2. Team size and skills needed
3. Dependencies and blockers
4. Estimated timeline
5. Risks and mitigations
6. Definition of done

Also identify:
- What can be built in parallel
- What should be prototyped/spiked first
- Technical debt that's acceptable in Phase 1 but must be addressed later
```

### Usage Notes

- Step 1 is the most important — don't rush it
- Architecture options (Step 2) prevent anchoring on the first idea
- Share the Step 4 implementation plan with your team for estimation
- Revisit Step 2 if you learn new requirements during detailed design

---

## Systematic Debugging Playbook

> A structured approach to diagnosing and fixing bugs, from reproduction to root cause to prevention.

### When to Use

- Bug that's hard to reproduce
- Production incident requiring methodical investigation
- Performance regression with unclear cause
- Flaky tests or intermittent failures

---

### Step 1: Bug Characterization

```
Help me systematically debug this issue:

**Symptom:** {{WHAT_IS_HAPPENING}}
**Expected behavior:** {{WHAT_SHOULD_HAPPEN}}
**Environment:** {{WHERE_IT_HAPPENS}} (prod, staging, local, specific OS/browser)
**Frequency:** {{ALWAYS | INTERMITTENT | FIRST_TIME}}
**First noticed:** {{WHEN}}
**Recent changes:** {{WHAT_CHANGED}} (deploys, config changes, data changes, dependency updates)

Error output:
```
{{ERROR_MESSAGES_STACK_TRACES_LOGS}}
```

Based on this, help me:
1. Classify the bug type (logic error, race condition, resource exhaustion, configuration, dependency)
2. Generate 3-5 hypotheses ranked by likelihood
3. For each hypothesis, provide a specific diagnostic step to confirm or rule it out
4. Identify what additional information would narrow it down fastest
```

---

### Step 2: Isolation & Reproduction

```
I'm trying to reproduce this bug:

**Hypothesis:** {{MOST_LIKELY_CAUSE_FROM_STEP_1}}
**System:** {{RELEVANT_ARCHITECTURE}}

Help me create:
1. A minimal reproduction case — smallest possible code/config that triggers the bug
2. Environment setup instructions to match the failing environment
3. A test that currently fails and will pass once the bug is fixed
4. Logging/instrumentation to add if the bug can't be reproduced locally

If this is an intermittent bug, also suggest:
- Race condition detection techniques
- Load/stress test to trigger timing-dependent failures
- State combinations to explore systematically
```

---

### Step 3: Root Cause Analysis

```
I've confirmed the bug is caused by:

**Root cause:** {{WHAT_YOU_FOUND}}
**Evidence:** {{HOW_YOU_CONFIRMED_IT}}

Now help me:
1. Understand why this was possible — what guard was missing?
2. Determine the blast radius — what else might be affected by the same root cause?
3. Design the fix with the smallest possible change
4. Identify regression tests to prevent recurrence
5. Write a brief post-mortem summary:
   - Timeline
   - Impact
   - Root cause
   - Fix
   - Follow-up actions to prevent similar issues
```

### Usage Notes

- Resist the urge to jump to Step 3 — Step 1's hypothesis ranking saves time
- "What changed recently" is the single most useful diagnostic question
- The post-mortem in Step 3 is invaluable for team learning — don't skip it
- For production incidents, add timestamps to everything

---

## Python-Specific Prompts

> Prompts tailored for Python development best practices.

---

### Project Scaffolding

```
Scaffold a Python project with the following specs:

**Project type:** {{TYPE}} (e.g., CLI tool, REST API, library/package, ETL script, ML pipeline)
**Python version:** {{VERSION}} (e.g., 3.11+)
**Package manager:** {{pip | poetry | uv | pdm}}
**Key dependencies:** {{LIST_MAIN_LIBRARIES}}

Generate:
1. Directory structure following Python packaging best practices
2. pyproject.toml with all config (no setup.py)
3. Makefile or justfile with common commands (test, lint, format, run)
4. Pre-commit config with ruff, mypy, and black/ruff-format
5. GitHub Actions CI workflow
6. Dockerfile (if applicable)
7. Example module with type hints demonstrating the project pattern
8. Corresponding test file with pytest fixtures
```

---

### Type Annotation Retrofit

```
Add comprehensive type annotations to this Python code:

```python
{{YOUR_CODE}}
```

Requirements:
- Use modern Python typing (3.10+ syntax: X | Y instead of Union[X, Y])
- Add return types to all functions
- Type all function parameters
- Use TypedDict for complex dict structures
- Use Protocol for duck typing where appropriate
- Add Generic types where it improves reusability
- Flag any places where the types reveal potential bugs
- Ensure mypy --strict would pass
```

---

### Async Conversion

```
Convert this synchronous Python code to async:

```python
{{YOUR_CODE}}
```

**Async framework:** {{asyncio | trio | anyio}}
**I/O libraries to convert:** {{requests→httpx | psycopg2→asyncpg | etc.}}

Provide:
1. Async version with proper await points
2. Explanation of concurrency opportunities (what can run in parallel)
3. Connection pool / session management for async
4. Error handling adjustments needed for async context
5. Performance comparison notes (when async helps vs. doesn't)
```

---

### Performance Profiling Guide

```
This Python code is too slow. Help me profile and optimize it:

```python
{{YOUR_CODE}}
```

**Current performance:** {{METRIC}} (e.g., "takes 45s for 1M rows")
**Target performance:** {{TARGET}}

Walk me through:
1. Which profiling tool to use (cProfile, line_profiler, memory_profiler, py-spy)
2. The exact commands to run the profiler
3. How to interpret the output
4. Top 3 most likely bottlenecks based on code inspection
5. Optimization strategies for each bottleneck:
   - Algorithm improvements
   - Data structure changes
   - Caching opportunities
   - Vectorization with numpy/pandas
   - Parallelization with multiprocessing/concurrent.futures
```

### Usage Notes

- Project scaffolding: specify your org's conventions if they differ from defaults
- Type annotations: feed modules one at a time for best results
- Async: not everything benefits from async — the prompt helps identify where it matters

---

## Docker & DevOps Prompts

> Prompts for containerization, CI/CD, and infrastructure.

---

### Dockerfile Optimization

```
Optimize this Dockerfile for {{GOAL}} (e.g., smaller image size, faster builds, security):

```dockerfile
{{YOUR_DOCKERFILE}}
```

**Application type:** {{TYPE}} (e.g., Python API, Node.js app, Go binary)
**Current image size:** {{SIZE}}
**Build time:** {{DURATION}}

Provide:
1. Optimized Dockerfile with comments explaining each improvement
2. Multi-stage build if applicable
3. Layer caching strategy for fastest rebuilds
4. Security hardening (non-root user, minimal base image, no secrets in layers)
5. .dockerignore recommendations
6. Before/after comparison of image size and build time
```

---

### CI/CD Pipeline Design

```
Design a CI/CD pipeline for the following project:

**Repository:** {{MONO_OR_MULTI_REPO}}
**Language(s):** {{LANGUAGES}}
**Platform:** {{GitHub Actions | GitLab CI | Jenkins | CircleCI}}
**Deployment target:** {{AWS | GCP | Azure | K8s | bare metal}}
**Environments:** {{dev | staging | prod}}

The pipeline should include:
1. Code quality gates (lint, format, type check)
2. Test stages (unit → integration → e2e)
3. Security scanning (SAST, dependency audit, container scan)
4. Build and push artifacts/images
5. Deployment with rollback capability
6. Environment promotion workflow
7. Notification hooks (Slack, email)

Provide the complete pipeline YAML/config with comments.
```

---

### Infrastructure as Code

```
Write {{TOOL}} (e.g., Terraform, Pulumi, CDK) code for:

**Infrastructure:** {{WHAT_TO_PROVISION}}
**Cloud provider:** {{AWS | GCP | Azure}}
**Environment strategy:** {{HOW_ENVS_ARE_SEPARATED}} (e.g., separate accounts, namespaces, workspaces)

Requirements:
- Modular and reusable (use modules/constructs)
- Environment-specific variables with sensible defaults
- State management configuration
- Tagging strategy for cost tracking
- Security best practices (least privilege IAM, encryption at rest)
- Output the important values (endpoints, IDs) for downstream use
```

### Usage Notes

- Always include the current Dockerfile when optimizing — context matters
- For CI/CD, mention if you use monorepo tooling (Nx, Turborepo, Bazel)
- IaC prompts work best when you specify the exact cloud services needed
