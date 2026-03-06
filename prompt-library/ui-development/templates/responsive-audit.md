# Responsive Design Audit Template

> Audit existing UI code for responsive design issues.

## Prompt

```
Audit the following component/page for responsive design issues:

```{{LANGUAGE}}
{{YOUR_CODE}}
```

**Current breakpoints used:** {{BREAKPOINTS}}
**Known issues:** {{ANY_REPORTED_PROBLEMS}}
**Target devices:** {{DEVICES}} (e.g., iPhone SE, iPad, 1440p desktop, 4K)

Check for:
1. **Fixed widths** — Elements with px widths that break on small screens
2. **Overflow** — Content that overflows its container (horizontal scroll)
3. **Touch targets** — Interactive elements smaller than 44x44px on mobile
4. **Typography** — Font sizes that don't scale, text that gets cut off
5. **Images** — Missing responsive images, images that don't resize
6. **Spacing** — Margins/padding that create too much whitespace on mobile
7. **Navigation** — Desktop nav that doesn't collapse on mobile
8. **Tables** — Wide tables that break on narrow screens
9. **Modals/overlays** — Dialogs that don't work on mobile viewports
10. **Orientation** — Layout broken in landscape on mobile

For each issue, provide:
- The specific line(s) of code
- Why it's a problem
- The fix
```

## Usage Notes

- Run this on every new page before launch
- Include the CSS/styles — many responsive issues live there
- Pair with browser DevTools device mode for visual confirmation
