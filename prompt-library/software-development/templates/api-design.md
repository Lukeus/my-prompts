# API Design Template

> Design a REST or GraphQL API for a feature or service.

## Prompt

```
Design an API for the following feature:

**Feature:** {{FEATURE_DESCRIPTION}}
**API style:** {{REST | GraphQL | gRPC}}
**Authentication:** {{JWT | API key | OAuth2 | session}}
**Consumers:** {{WHO_WILL_CALL_THIS}} (e.g., web frontend, mobile app, internal service)

**Core entities:**
- {{ENTITY_1}}: {{BRIEF_DESCRIPTION}}
- {{ENTITY_2}}: {{BRIEF_DESCRIPTION}}

**Key operations:**
- {{OPERATION_1}}
- {{OPERATION_2}}
- {{OPERATION_3}}

Provide:
1. Endpoint/schema definitions with request/response shapes
2. HTTP methods, status codes, and error response format
3. Pagination strategy for list endpoints
4. Rate limiting recommendations
5. Versioning strategy
6. Example curl commands or queries for each endpoint
7. OpenAPI spec snippet (for REST) or schema definition (for GraphQL)

[OPTIONAL: Must support {{SPECIAL_REQUIREMENT}} such as webhooks, file uploads, or real-time subscriptions]
```

## Usage Notes

- Be specific about consumers — mobile APIs need different pagination than internal services
- Include error response format upfront to avoid inconsistency later
- Pair with `testing-strategy.md` to generate integration tests for the API
