# README Generator

> Create a professional README from codebase analysis.

## Prompt

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

## Usage Notes

- The package manifest is the most information-dense input — always include it
- CI config reveals the build/test process better than most documentation
- If the project has multiple packages/services, generate a root README that links to sub-READMEs
