# Form Builder Template

> Generate a complete form with validation, error handling, and accessibility.

## Prompt

```
Build a form for {{PURPOSE}} (e.g., user registration, checkout, settings page):

**Framework:** {{FRAMEWORK}}
**Form library:** {{react-hook-form | formik | vee-validate | native | zod}}
**Validation library:** {{zod | yup | joi | native}}

**Fields:**
| Field | Type | Required | Validation Rules |
|-------|------|----------|-----------------|
| {{NAME}} | {{text/email/select/checkbox/etc.}} | {{yes/no}} | {{rules}} |
| {{NAME}} | {{TYPE}} | {{REQ}} | {{RULES}} |

**Submission:**
- Endpoint: {{API_ENDPOINT}}
- Method: {{POST | PUT | PATCH}}
- Success behavior: {{WHAT_HAPPENS}}
- Error behavior: {{WHAT_HAPPENS}}

Requirements:
1. Client-side validation with inline error messages
2. Server-side error handling (display API errors per field)
3. Loading state during submission (disable form, show spinner)
4. Prevent double submission
5. Proper label -> input associations
6. Autofocus on first field
7. Tab order follows visual order
8. Announce errors to screen readers (aria-live region)

[OPTIONAL: Multi-step wizard with progress indicator]
[OPTIONAL: Auto-save draft to localStorage]
```

## Usage Notes

- The field table makes requirements unambiguous — fill it out completely
- Always include both client and server error handling
- Multi-step forms need careful state management — use the optional flag
