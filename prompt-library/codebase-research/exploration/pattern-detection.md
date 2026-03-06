# Pattern Detection Prompt

> Identify design patterns, anti-patterns, and conventions used in a codebase.

## Prompt

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

## Usage Notes

- Feed in 5-10 representative files for pattern detection
- Include test files — testing patterns reveal a lot about code quality
- The "conventions" section is gold for new team members
