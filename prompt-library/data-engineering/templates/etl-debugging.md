# ETL Debugging Template

> Diagnose and fix a failing or misbehaving data pipeline.

## Prompt

```
I have a data pipeline that is {{SYMPTOM}}. Help me debug it.

**Pipeline description:** {{BRIEF_DESCRIPTION}}
**Orchestrator:** {{TOOL}} (e.g., Airflow, Prefect, Dagster, Step Functions)
**Error message (if any):**
```
{{ERROR_OUTPUT}}
```
**What changed recently:** {{RECENT_CHANGES}}
**Expected behavior:** {{WHAT_SHOULD_HAPPEN}}
**Actual behavior:** {{WHAT_IS_HAPPENING}}

Walk me through:
1. Most likely root causes ranked by probability
2. Diagnostic queries or commands to confirm each hypothesis
3. The fix for the most probable cause
4. How to prevent this class of failure in the future
```

## Usage Notes

- Include the full stack trace or error log when possible
- "What changed recently" is often the most diagnostic field — be thorough
- Symptoms: "producing duplicates", "missing data", "timing out", "silently dropping rows"
