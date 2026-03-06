# Schema Design Template

> Design a data model for a specific domain or use case.

## Prompt

```
Design a data schema for the following use case:

**Domain:** {{DOMAIN}} (e.g., e-commerce orders, IoT sensor data, SaaS billing)
**Modeling approach:** {{APPROACH}} (e.g., star schema, snowflake, OBT, Data Vault, normalized)
**Target warehouse:** {{WAREHOUSE}} (e.g., Snowflake, BigQuery, Postgres, Databricks)
**Key business questions this must answer:**
- {{QUESTION_1}}
- {{QUESTION_2}}
- {{QUESTION_3}}

Provide:
1. Entity-relationship diagram (mermaid or text description)
2. DDL statements for all tables
3. Explanation of grain for each fact table
4. Slowly changing dimension strategy where applicable
5. Indexing and partitioning recommendations
6. Sample queries that answer the business questions above
```

## Usage Notes

- Specify "Data Vault" if you need auditability and flexibility
- Specify "OBT (One Big Table)" for analytics-heavy, low-join environments
- Add `[OPTIONAL: Include CDC tracking columns]` if you need change data capture support
