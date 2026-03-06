# Evaluation Test Generator

> Create test cases to measure prompt quality before deploying.

## Prompt

```
Generate evaluation test cases for this prompt:

**Prompt being tested:**
```
{{YOUR_PROMPT}}
```

**What "good" looks like:** {{CRITERIA_FOR_SUCCESS}}
**What "bad" looks like:** {{COMMON_FAILURES}}

Generate test cases in these categories:

1. **Happy path** (5 cases) — Standard inputs that should produce ideal outputs
2. **Edge cases** (5 cases) — Unusual but valid inputs (empty, very long, special characters, multilingual)
3. **Adversarial** (3 cases) — Inputs designed to break the prompt or produce bad output
4. **Ambiguous** (3 cases) — Inputs where the correct behavior isn't obvious

For each test case, provide:
- Input
- Expected output (or acceptable output range)
- What specifically to check (format, accuracy, completeness, tone)
- Pass/fail criteria

Also suggest:
- Automated checks that can be scripted (regex, JSON schema, keyword presence)
- Checks that require human judgment (quality, helpfulness, appropriateness)
```

## Usage Notes

- Run evals before and after every prompt change
- Adversarial cases are the highest-signal tests — don't skip them
- Automate what you can, but budget time for human review of edge cases
- Track eval scores over time to catch regressions
