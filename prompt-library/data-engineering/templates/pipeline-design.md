# Pipeline Design Template

> Quick prompt for designing a data pipeline from scratch.

## Prompt

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

## Usage Notes

- Adjust the optional section for your specific pain points
- Works well as a starting point before diving into implementation prompts
- Pair with the `data-quality-checks.md` template for end-to-end coverage
