# Data Modeling Review Playbook

> Systematic review of an existing data model to find issues, inefficiencies, and improvement opportunities.

## When to Use

- Inheriting a data warehouse from another team
- Performance has degraded as data volume grew
- Business requirements have shifted and the model feels wrong
- Preparing for a modeling standards audit

---

## Step 1: Model Inventory

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

## Step 2: Relationship & Dependency Analysis

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

## Step 3: Performance & Anti-pattern Audit

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

## Step 4: Recommendations Report

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

## Usage Notes

- Feed actual DDL into these prompts for the best results
- Step 3 works especially well if you also provide slow query examples
- The final report from Step 4 makes a great artifact for stakeholder buy-in
