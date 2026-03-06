# Error Handling Design Template

> Design a consistent error handling strategy for an application or service.

## Prompt

```
Design an error handling strategy for the following system:

**Application type:** {{TYPE}} (e.g., REST API, CLI tool, background worker, web app)
**Language:** {{LANGUAGE}}
**Current approach:** {{HOW_ERRORS_ARE_HANDLED_NOW}} (or "none — starting fresh")

Provide:
1. Error classification taxonomy (e.g., validation, auth, not found, internal, external dependency)
2. Custom error/exception class hierarchy
3. Error response format (for APIs) or error display approach (for UIs)
4. Logging strategy — what to log at each level (error, warn, info)
5. Retry and circuit breaker patterns for recoverable errors
6. Error code catalog with human-readable messages
7. How to propagate errors across service boundaries

Implementation requirements:
- Errors should be actionable — tell the caller what to do
- Internal details (stack traces, SQL) must never leak to clients
- Errors should be easy to search in logs (structured logging format)
- Include correlation IDs for tracing errors across services
```

## Usage Notes

- This is a foundational prompt — run it early in a project
- The error code catalog becomes a reference for your whole team
- Pair with monitoring/alerting setup for production readiness
