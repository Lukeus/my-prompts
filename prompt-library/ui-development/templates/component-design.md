# Component Design Template

> Design and build a reusable UI component from a description.

## Prompt

```
Build a {{COMPONENT_TYPE}} component with the following requirements:

**Framework:** {{React | Vue | Svelte | Angular | vanilla}}
**Styling:** {{Tailwind | CSS Modules | styled-components | plain CSS}}
**Component name:** {{NAME}}

**Behavior:**
{{DESCRIBE_WHAT_IT_DOES}}

**Props/inputs:**
- {{PROP_1}}: {{TYPE}} — {{DESCRIPTION}}
- {{PROP_2}}: {{TYPE}} — {{DESCRIPTION}}

**States to handle:**
- Default / empty
- Loading
- Error
- Populated / success
- Disabled (if interactive)

**Accessibility requirements:**
- Keyboard navigable
- Screen reader friendly (proper ARIA labels)
- Sufficient color contrast
- Focus management

Provide:
1. Component code with TypeScript types
2. All state variations
3. Responsive behavior (mobile, tablet, desktop)
4. Usage example with sample props
5. Unit test covering key interactions
```

## Usage Notes

- Always specify the states — it forces complete implementations
- Accessibility requirements prevent the most common UI/UX issues
- Add `[OPTIONAL: Include Storybook story]` for design system components
