# Dependency Mapping Prompt

> Map internal and external dependencies to understand coupling and risk.

## Prompt

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

## Usage Notes

- For large projects, focus on one service or package at a time
- The "deeply coupled" assessment helps prioritize migration efforts
- Circular dependencies are almost always a design smell — flag them
