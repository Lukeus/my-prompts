# Data Engineering Prompts Reference

## Table of Contents

1. [Pipeline Design Template](#pipeline-design-template)
2. [Data Quality Checks Template](#data-quality-checks-template)
3. [Schema Design Template](#schema-design-template)
4. [ETL Debugging Template](#etl-debugging-template)
5. [SQL Optimization Template](#sql-optimization-template)
6. [Data Migration Playbook](#data-migration-playbook)
7. [Data Modeling Review Playbook](#data-modeling-review-playbook)
8. [dbt-Specific Prompts](#dbt-specific-prompts)
9. [Airflow Orchestration Prompts](#airflow-orchestration-prompts)

---

## Pipeline Design Template

> Quick prompt for designing a data pipeline from scratch.

### Prompt

```
Design a data pipeline with the following requirements:

**Source(s):** {{DATA_SOURCES}} (e.g., PostgreSQL, REST API, S3 bucket, Kafka topic)
**Destination:** {{TARGET_SYSTEM}} (e.g., Snowflake, BigQuery, Redshift, Delta Lake)
**Volume:** {{DATA_VOLUME}} (e.g., 10GB/day, 1M events/hour)
**Freshness requirement:** {{LATENCY}} (e.g., real-time, hourly, daily)
**Data format:** {{FORMAT}} (e.g., JSON, Parquet, CSV, Avro)

For this pipeline, provide:
1. Architecture diagram (described in text or mermaid)
2. Recommended orchestration tool and why
3. Schema design for the destination
4. Error handling and retry strategy
5. Monitoring and alerting approach
6. Estimated cost considerations

[OPTIONAL: The pipeline must handle {{SPECIFIC_CHALLENGE}} such as late-arriving data, schema evolution, or deduplication.]
```

### Usage Notes

- Adjust the optional section for your specific pain points
- Works well as a starting point before diving into implementation prompts
- Pair with the `data-quality-checks.md` template for end-to-end coverage

---

## Data Quality Checks Template

> Generate comprehensive data quality validations for a table or dataset.

### Prompt

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

### Usage Notes

- Great for bootstrapping a data quality framework on new tables
- Output can be adapted into Great Expectations, dbt tests, or Soda checks
- Run this for each critical table in your warehouse

---

## Schema Design Template

> Design a data model for a specific domain or use case.

### Prompt

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

### Usage Notes

- Specify "Data Vault" if you need auditability and flexibility
- Specify "OBT (One Big Table)" for analytics-heavy, low-join environments
- Add `[OPTIONAL: Include CDC tracking columns]` if you need change data capture support

---

## ETL Debugging Template

> Diagnose and fix a failing or misbehaving data pipeline.

### Prompt

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

### Usage Notes

- Include the full stack trace or error log when possible
- "What changed recently" is often the most diagnostic field — be thorough
- Symptoms: "producing duplicates", "missing data", "timing out", "silently dropping rows"

---

## SQL Optimization Template

> Optimize a slow query with targeted improvements.

### Prompt

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

### Usage Notes

- Always include the query plan if you have it — dramatically improves suggestions
- For Snowflake, mention clustering keys; for BigQuery, mention partition/cluster columns
- Pair with `schema-design.md` if the underlying model needs rethinking

---

## Data Migration Playbook

> End-to-end workflow for migrating data between systems with zero (or minimal) downtime.

### When to Use

- Moving from one warehouse to another (e.g., Redshift → Snowflake)
- Migrating from legacy ETL to modern stack (e.g., stored procs → dbt)
- Re-platforming a database (e.g., Oracle → Postgres)
- Consolidating multiple data sources into a single platform

---

### Phase 1: Discovery & Assessment

```
I'm planning a data migration with the following context:

**Source system:** {{SOURCE}} (version, type, approximate size)
**Target system:** {{TARGET}}
**Number of tables/objects:** {{COUNT}}
**Total data volume:** {{VOLUME}}
**Active users/consumers:** {{WHO_DEPENDS_ON_THIS}}
**Compliance requirements:** {{ANY_REGULATORY_CONSTRAINTS}}

Perform a migration assessment:
1. Identify the highest-risk tables (large, complex, heavily used)
2. Map data type incompatibilities between source and target
3. List features used in source that don't exist in target
4. Estimate migration timeline based on volume and complexity
5. Identify dependencies that must migrate together (foreign keys, views, procs)
6. Recommend a migration strategy: big bang, trickle, or parallel run
```

---

### Phase 2: Schema Translation

```
Translate the following schema from {{SOURCE_DIALECT}} to {{TARGET_DIALECT}}:

```sql
{{SOURCE_DDL}}
```

Requirements:
- Preserve all constraints and relationships
- Use target-native best practices (partitioning, clustering, etc.)
- Flag any features that require workarounds in the target
- Add comments explaining non-obvious translation decisions
- Include migration-specific columns (e.g., _migrated_at, _source_id) if appropriate
```

---

### Phase 3: Data Validation

```
Generate a comprehensive data validation plan for a migration from {{SOURCE}} to {{TARGET}}.

For each migrated table, produce validation queries that check:
1. Row counts match (exact or within tolerance)
2. Checksum/hash comparison on key columns
3. Min/max/avg of numeric columns match
4. Null counts match per column
5. Distinct value counts for categorical columns
6. Date range boundaries are preserved
7. Sample row comparison (random 1000 rows)

Output the queries for both source and target so results can be compared side by side.
```

---

### Phase 4: Cutover Planning

```
Create a cutover runbook for migrating from {{SOURCE}} to {{TARGET}}.

Context:
- **Acceptable downtime window:** {{WINDOW}}
- **Rollback requirement:** {{ROLLBACK_NEEDS}}
- **Number of dependent applications:** {{APP_COUNT}}

The runbook should include:
1. Pre-cutover checklist (validations, backups, notifications)
2. Step-by-step cutover procedure with estimated times
3. Verification steps at each stage
4. Rollback procedure if something goes wrong
5. Post-cutover monitoring plan for the first 24/48/72 hours
6. Communication template for stakeholders
```

### Usage Notes

- Run phases sequentially — each builds on the previous
- Phase 3 (validation) is the most critical — don't skip it
- Keep the cutover runbook in a shared doc so the whole team can follow along
- Consider running Phase 3 validation in parallel with ongoing source operations before cutover

---

## Data Modeling Review Playbook

> Systematic review of an existing data model to find issues, inefficiencies, and improvement opportunities.

### When to Use

- Inheriting a data warehouse from another team
- Performance has degraded as data volume grew
- Business requirements have shifted and the model feels wrong
- Preparing for a modeling standards audit

---

### Step 1: Model Inventory

```
I'm reviewing a data model in {{WAREHOUSE}}. Here are the key tables:

{{LIST_OF_TABLES_WITH_BRIEF_DESCRIPTIONS}}

For each table, analyze:
1. What is the grain? (What does one row represent?)
2. Is this a fact, dimension, bridge, or staging table?
3. Are there any naming convention inconsistencies?
4. What modeling pattern is being used (star, snowflake, OBT, vault)?
5. Are there signs of organic/unplanned growth (e.g., catch-all columns, inconsistent prefixes)?

Provide a summary scorecard: what's working well and what needs attention.
```

---

### Step 2: Relationship & Dependency Analysis

```
Given these table DDLs:

```sql
{{DDL_FOR_KEY_TABLES}}
```

Analyze the relationships:
1. Map all foreign key relationships (explicit and implicit)
2. Identify circular dependencies
3. Find orphan tables with no inbound or outbound references
4. Detect fan-out traps (joins that unexpectedly multiply rows)
5. Check for missing relationships that business logic implies
6. Produce a mermaid ER diagram of the core model
```

---

### Step 3: Performance & Anti-pattern Audit

```
Review this data model for performance anti-patterns:

{{DDL_OR_DESCRIPTION}}

Check for:
1. **Over-normalization** — Too many joins needed for common queries
2. **Under-normalization** — Update anomalies, redundant data
3. **Missing partitioning** — Large tables without time or key-based partitions
4. **Wide tables** — Tables with 100+ columns that should be split
5. **Implicit types** — Dates stored as strings, IDs with mixed types
6. **Accumulating snapshots** — Fact tables that get updated instead of appended
7. **Missing surrogate keys** — Natural keys used as primary keys in dimensions

For each issue found, explain the impact and recommend a fix with migration steps.
```

---

### Step 4: Recommendations Report

```
Based on the following findings from a data model review:

{{SUMMARY_OF_FINDINGS_FROM_STEPS_1_3}}

Produce a prioritized recommendations report:
1. **Critical** — Issues causing data quality problems or significant performance impact
2. **High** — Anti-patterns that will become problems as data grows
3. **Medium** — Modeling improvements for maintainability
4. **Low** — Naming conventions, documentation gaps

For each recommendation, include:
- What to change
- Why it matters
- Estimated effort (hours/days)
- Risk of the change
- Suggested implementation order
```

### Usage Notes

- Feed actual DDL into these prompts for the best results
- Step 3 works especially well if you also provide slow query examples
- The final report from Step 4 makes a great artifact for stakeholder buy-in

---

## dbt-Specific Prompts

> Prompts tailored for dbt (data build tool) development workflows.

---

### Model Generation

```
Generate a dbt model for the following transformation:

**Source tables:** {{SOURCE_TABLES}}
**Target model name:** {{MODEL_NAME}}
**Model type:** {{staging | intermediate | mart}}
**Materialization:** {{view | table | incremental | ephemeral}}
**Business logic:**
{{DESCRIBE_THE_TRANSFORMATION}}

Include:
- Proper CTEs with descriptive names
- Column renaming to match naming conventions (snake_case)
- Type casting where appropriate
- A YAML schema file with column descriptions and tests
- The appropriate ref() and source() macros
[OPTIONAL: Use incremental materialization with {{INCREMENTAL_STRATEGY}} strategy]
```

---

### Test Generation

```
Generate dbt tests for the model `{{MODEL_NAME}}` with these columns:

{{COLUMN_LIST_WITH_TYPES}}

Produce:
1. Schema tests in YAML (unique, not_null, accepted_values, relationships)
2. Custom singular tests for complex business rules:
   - {{BUSINESS_RULE_1}}
   - {{BUSINESS_RULE_2}}
3. Generic test macros for reusable validation patterns
4. Freshness tests for source tables

Follow dbt best practices: test at the right granularity, don't over-test obvious things.
```

---

### Incremental Model Debugging

```
My dbt incremental model is {{PROBLEM}}:

```sql
{{MODEL_SQL}}
```

**Incremental strategy:** {{merge | delete+insert | insert_overwrite | append}}
**is_incremental() filter:**
```sql
{{THE_WHERE_CLAUSE}}
```
**Warehouse:** {{WAREHOUSE}}

Diagnose:
1. Is the incremental logic correct for this use case?
2. Are there late-arriving records that slip through?
3. Could there be duplicates from the merge strategy?
4. Is the full refresh producing different results than incremental? Why?
5. Provide a corrected version with explanations.
```

---

### Macro Writing

```
Write a dbt macro that does the following:

**Purpose:** {{WHAT_THE_MACRO_SHOULD_DO}}
**Parameters:** {{INPUT_PARAMETERS}}
**Example usage:** {{HOW_IT_SHOULD_BE_CALLED}}

Requirements:
- Handle edge cases (nulls, empty strings, type mismatches)
- Work across {{WAREHOUSE_DIALECTS}} (e.g., Snowflake + BigQuery)
- Include Jinja comments explaining the logic
- Provide a test model that demonstrates usage
```

---

### Project Structure Review

```
Review my dbt project structure and suggest improvements:

```
{{TREE_OUTPUT_OF_DBT_PROJECT}}
```

My dbt_project.yml materialization config:
```yaml
{{DBT_PROJECT_YML_EXCERPT}}
```

Evaluate:
1. Does the staging → intermediate → mart layering make sense?
2. Are models in the right directories?
3. Is the materialization strategy appropriate per layer?
4. Are there models that should be refactored or consolidated?
5. Does the naming convention follow dbt best practices?
6. Recommend a target structure if changes are needed.
```

### Usage Notes

- Always include your `dbt_project.yml` config when asking about project structure
- For incremental debugging, run `dbt run --full-refresh` and compare results
- Macro prompts work best when you provide the exact SQL dialect you need

---

## Airflow Orchestration Prompts

> Prompts for building, debugging, and optimizing Apache Airflow DAGs.

---

### DAG Design

```
Design an Airflow DAG for the following workflow:

**Pipeline name:** {{DAG_ID}}
**Schedule:** {{CRON_OR_DESCRIPTION}} (e.g., "daily at 6am UTC", "0 6 * * *")
**Tasks:**
{{NUMBERED_LIST_OF_TASKS_WITH_DEPENDENCIES}}

**Requirements:**
- Retry policy: {{RETRIES_AND_DELAY}}
- SLA: {{EXPECTED_COMPLETION_TIME}}
- Notifications: {{SLACK | EMAIL | PAGERDUTY}}
- Concurrency limits: {{MAX_PARALLEL_TASKS}}

Provide:
1. Complete DAG Python file using TaskFlow API (Airflow 2.x+)
2. Proper dependency chain using >> operators
3. Error handling with on_failure_callback
4. XCom usage if tasks need to share data
5. Connection and variable references (not hardcoded secrets)
```

---

### DAG Debugging

```
My Airflow DAG is {{PROBLEM}} (e.g., stuck, failing, not triggering, tasks running out of order).

**Airflow version:** {{VERSION}}
**Executor:** {{CeleryExecutor | KubernetesExecutor | LocalExecutor}}
**Error from logs:**
```
{{LOG_OUTPUT}}
```

**DAG code (relevant section):**
```python
{{DAG_CODE}}
```

Help me:
1. Identify the root cause from the logs
2. Check for common Airflow gotchas (import errors, circular deps, timezone issues)
3. Provide the fix
4. Suggest monitoring to catch this earlier next time
```

---

### Dynamic DAG Generation

```
I need to generate Airflow DAGs dynamically for {{USE_CASE}}.

**Pattern:** {{DESCRIPTION}} (e.g., one DAG per client, one DAG per data source, one DAG per table)
**Config source:** {{WHERE_CONFIG_LIVES}} (e.g., YAML file, Airflow Variable, database table)
**Number of expected DAGs:** {{APPROXIMATE_COUNT}}

Build a dynamic DAG factory that:
1. Reads configuration from {{CONFIG_SOURCE}}
2. Generates one DAG per {{ENTITY}}
3. Handles additions/removals without code changes
4. Maintains independent schedules and retry policies per DAG
5. Doesn't cause DAG bag import slowness at scale
```

### Usage Notes

- Always specify your Airflow version — the API changed significantly between 1.x and 2.x
- For Kubernetes executor issues, include pod spec and resource limits
- Dynamic DAG generation can slow down the scheduler — monitor parse times
