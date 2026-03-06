# dbt-Specific Prompts

> Prompts tailored for dbt (data build tool) development workflows.

---

## Model Generation

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

## Test Generation

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

## Incremental Model Debugging

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

## Macro Writing

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

## Project Structure Review

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
1. Does the staging -> intermediate -> mart layering make sense?
2. Are models in the right directories?
3. Is the materialization strategy appropriate per layer?
4. Are there models that should be refactored or consolidated?
5. Does the naming convention follow dbt best practices?
6. Recommend a target structure if changes are needed.
```

## Usage Notes

- Always include your `dbt_project.yml` config when asking about project structure
- For incremental debugging, run `dbt run --full-refresh` and compare results
- Macro prompts work best when you provide the exact SQL dialect you need
