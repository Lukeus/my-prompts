# Code Review Template

> Get a thorough code review with actionable feedback.

## Prompt

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

## Usage Notes

- Include surrounding context (imports, related functions) for better reviews
- Specify your team's conventions if they differ from language defaults
- Works best with functions/classes under ~200 lines — split large reviews
