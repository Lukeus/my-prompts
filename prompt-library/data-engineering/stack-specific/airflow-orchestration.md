# Airflow Orchestration Prompts

> Prompts for building, debugging, and optimizing Apache Airflow DAGs.

---

## DAG Design

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

## DAG Debugging

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

## Dynamic DAG Generation

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

## Usage Notes

- Always specify your Airflow version — the API changed significantly between 1.x and 2.x
- For Kubernetes executor issues, include pod spec and resource limits
- Dynamic DAG generation can slow down the scheduler — monitor parse times
