# Impact Analysis Prompt

> Before making a change, understand what it will affect.

## Prompt

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

## Usage Notes

- Include callers and dependents in the code context — not just the code being changed
- The "transitive dependents" question catches non-obvious breakage
- The deployment strategy recommendation is especially valuable for high-risk changes
