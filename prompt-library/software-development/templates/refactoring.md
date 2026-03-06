# Refactoring Template

> Refactor code to improve structure without changing behavior.

## Prompt

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

## Usage Notes

- "Don't mix bug fixes with refactoring" keeps changes reviewable
- For large refactors, ask for an incremental plan rather than a single big change
- Specify backward compatibility constraints to avoid breaking consumers
