# API Documentation Generator

> Generate complete API documentation from source code.

## Prompt

```
Generate API documentation from the following route/endpoint definitions:

**Framework:** {{FRAMEWORK}} (e.g., Express, FastAPI, Django, Spring Boot, Go Chi)
**Auth mechanism:** {{AUTH_TYPE}}

**Route code:**
```{{LANGUAGE}}
{{YOUR_ROUTE_HANDLERS}}
```

**Models/schemas used:**
```{{LANGUAGE}}
{{YOUR_DATA_MODELS}}
```

For each endpoint, document:

1. **Method & Path** — `GET /api/v1/users/{id}`
2. **Description** — What it does in one sentence
3. **Authentication** — Required? What role/scope?
4. **Path parameters** — Name, type, description, example
5. **Query parameters** — Name, type, required?, default, description
6. **Request body** — JSON schema with field descriptions and example
7. **Response** — Status codes with response body schema and example
8. **Error responses** — Each error status code with when it occurs
9. **Example request** — curl command
10. **Rate limiting** — If applicable

Output formats:
- Markdown (human-readable)
- OpenAPI 3.0 YAML snippet (machine-readable)

[OPTIONAL: Include SDK usage examples for {{LANGUAGE}}]
```

## Usage Notes

- Include the data models — they're essential for request/response schemas
- The curl examples make the docs immediately testable
- For GraphQL, adapt the template to document queries, mutations, and subscriptions
