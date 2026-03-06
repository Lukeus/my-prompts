# Testing Strategy Template

> Generate a comprehensive test plan and test code for a feature.

## Prompt

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

## Usage Notes

- Provide the function signatures at minimum — full implementation gives better tests
- Specify your mocking library preference (e.g., unittest.mock, sinon, testify/mock)
- Add `[OPTIONAL: Generate property-based tests using {{LIBRARY}}]` for thorough coverage
