# Layout from Description Template

> Generate a page layout or screen from a natural language description.

## Prompt

```
Create a {{PAGE_TYPE}} page layout based on this description:

**Framework:** {{FRAMEWORK}}
**Styling:** {{STYLING_APPROACH}}
**Description:**
{{NATURAL_LANGUAGE_DESCRIPTION_OF_THE_LAYOUT}}

**Breakpoints:**
- Mobile: 320px–767px
- Tablet: 768px–1023px
- Desktop: 1024px+

**Design tokens (if any):**
- Primary color: {{COLOR}}
- Font: {{FONT}}
- Border radius: {{RADIUS}}
- Spacing scale: {{SCALE}}

Requirements:
1. Semantic HTML structure
2. Fully responsive — describe the layout shift at each breakpoint
3. Skeleton/loading state for dynamic content areas
4. Proper heading hierarchy (h1 → h2 → h3)
5. Logical tab order for keyboard navigation

Output:
- Complete page component code
- Any child components needed
- CSS/styles
- Screenshot-like ASCII mockup showing the layout at desktop and mobile
```

## Usage Notes

- The more specific your description, the better the layout
- Include "above the fold" priorities for mobile
- Mention if you need the layout to match an existing design system
