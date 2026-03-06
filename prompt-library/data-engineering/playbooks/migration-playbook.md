# Data Migration Playbook

> End-to-end workflow for migrating data between systems with zero (or minimal) downtime.

## When to Use

- Moving from one warehouse to another (e.g., Redshift → Snowflake)
- Migrating from legacy ETL to modern stack (e.g., stored procs → dbt)
- Re-platforming a database (e.g., Oracle → Postgres)
- Consolidating multiple data sources into a single platform

---

## Phase 1: Discovery & Assessment

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

## Phase 2: Schema Translation

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

## Phase 3: Data Validation

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

## Phase 4: Cutover Planning

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

## Usage Notes

- Run phases sequentially — each builds on the previous
- Phase 3 (validation) is the most critical — don't skip it
- Keep the cutover runbook in a shared doc so the whole team can follow along
- Consider running Phase 3 validation in parallel with ongoing source operations before cutover
