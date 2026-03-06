# Monorepo Analysis Prompts

> Specialized prompts for understanding and navigating monorepo codebases.

---

## Monorepo Map

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

## Cross-Package Change Analysis

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

## Usage Notes

- Workspace config files (package.json workspaces, pnpm-workspace.yaml, nx.json) are essential input
- The dependency graph is the most valuable output — pin it somewhere visible
- For Nx repos, `nx graph` output can be fed directly into these prompts
