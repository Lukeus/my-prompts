# Repository Onboarding Prompt

> Quickly understand an unfamiliar codebase — architecture, patterns, and entry points.

## Prompt

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

## Usage Notes

- Feed in the directory tree (`tree -L 3`), key config files, and README for best results
- If the repo is too large, focus on the area relevant to your role
- Follow up with `dependency-mapping.md` for deeper analysis
