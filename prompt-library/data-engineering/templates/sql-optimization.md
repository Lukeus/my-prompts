# SQL Optimization Template

> Optimize a slow query with targeted improvements.

## Prompt

```
Optimize the following SQL query for performance:

**Warehouse:** {{WAREHOUSE}} (e.g., Snowflake, BigQuery, Postgres, Redshift)
**Current execution time:** {{DURATION}}
**Table sizes:** {{APPROXIMATE_ROW_COUNTS}}

```sql
{{YOUR_QUERY}}
```

[OPTIONAL: Here is the EXPLAIN/query plan output:
```
{{EXPLAIN_OUTPUT}}
```
]

Provide:
1. Analysis of why this query is slow
2. Optimized version of the query with comments explaining each change
3. Indexing or partitioning recommendations
4. Materialization strategy if the query is run frequently
5. Estimated improvement and any tradeoffs
```

## Usage Notes

- Always include the query plan if you have it — dramatically improves suggestions
- For Snowflake, mention clustering keys; for BigQuery, mention partition/cluster columns
- Pair with `schema-design.md` if the underlying model needs rethinking
