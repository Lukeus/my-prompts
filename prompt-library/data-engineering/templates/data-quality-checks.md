# Data Quality Checks Template

> Generate comprehensive data quality validations for a table or dataset.

## Prompt

```
Generate data quality checks for the following table/dataset:

**Table:** {{TABLE_NAME}}
**Key columns:** {{COLUMNS_WITH_TYPES}}
**Business context:** {{WHAT_THIS_DATA_REPRESENTS}}
**Known issues:** {{ANY_KNOWN_DATA_PROBLEMS}}

Produce checks in these categories:
1. **Completeness** — Null checks, required field validation
2. **Uniqueness** — Duplicate detection, primary key validation
3. **Freshness** — Staleness detection, expected update frequency
4. **Volume** — Row count anomalies, sudden drops or spikes
5. **Referential integrity** — Foreign key validation, orphan records
6. **Business rules** — Domain-specific constraints (e.g., prices > 0, dates in valid ranges)

For each check, provide:
- SQL query or pseudocode
- Severity level (critical / warning / info)
- Suggested alert threshold
- Recommended remediation action
```

## Usage Notes

- Great for bootstrapping a data quality framework on new tables
- Output can be adapted into Great Expectations, dbt tests, or Soda checks
- Run this for each critical table in your warehouse
