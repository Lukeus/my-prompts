# UI Development Prompts Reference

## Table of Contents

1. [Component Design Template](#component-design-template)
2. [Layout from Description Template](#layout-from-description-template)
3. [Form Builder Template](#form-builder-template)
4. [Responsive Design Audit Template](#responsive-design-audit-template)
5. [Design System Playbook](#design-system-playbook)
6. [Accessibility Audit Playbook](#accessibility-audit-playbook)
7. [React-Specific Prompts](#react-specific-prompts)

---

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

---

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
4. Proper heading hierarchy (h1 -> h2 -> h3)
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

---

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

---

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

---

# Design System Playbook

> Build a component library / design system from scratch or audit an existing one.

## When to Use

- Starting a new design system for your team
- Standardizing inconsistent UI across an application
- Creating a shared component library for multiple projects
- Auditing an existing design system for gaps

---

## Step 1: Design Token Foundation

```
Define a design token system for {{PROJECT_OR_BRAND}}:

**Brand colors:** {{PRIMARY_AND_SECONDARY_COLORS}}
**Typography:** {{FONT_FAMILY_PREFERENCES}}
**Existing brand guidelines:** {{LINK_OR_DESCRIPTION}}

Create a complete token set:
1. **Color palette** — Primary, secondary, neutral, semantic (success/warning/error/info), with light and dark variants
2. **Typography scale** — Font sizes, weights, line heights, letter spacing for headings, body, captions, labels
3. **Spacing scale** — Consistent spacing values (4px base or 8px base)
4. **Border radius** — Small, medium, large, full
5. **Shadows** — Elevation levels (sm, md, lg, xl)
6. **Breakpoints** — Mobile, tablet, desktop, wide
7. **Animation** — Duration and easing tokens

Output as:
- CSS custom properties (variables)
- Tailwind config extension
- JSON token file (compatible with Style Dictionary)
```

---

## Step 2: Core Component Inventory

```
Based on the design tokens from Step 1, define the core component set:

**Priority:** Build the minimum set needed for {{APPLICATION_TYPE}}.

For each component, specify:
1. All variants (size, color, state)
2. Props interface (TypeScript)
3. Accessibility requirements
4. Responsive behavior
5. Composition patterns (how it works with other components)

Start with these foundational components:
- Button (primary, secondary, ghost, destructive × sm, md, lg)
- Input (text, email, password, search, with label and error states)
- Select / Dropdown
- Checkbox / Radio
- Card
- Modal / Dialog
- Toast / Notification
- Badge / Tag
- Avatar
- Skeleton / Loading

Provide the full spec as a component matrix table.
```

---

## Step 3: Implementation

```
Implement the {{COMPONENT_NAME}} component from this spec:

{{SPEC_FROM_STEP_2}}

**Framework:** {{FRAMEWORK}}
**Styling:** {{APPROACH}} using design tokens from Step 1
**Testing:** {{TEST_FRAMEWORK}}

Provide:
1. Component code with all variants
2. TypeScript types / prop definitions
3. Storybook stories showing every variant and state
4. Unit tests for interactive behavior
5. Usage documentation with examples
6. Dos and don'ts for usage guidance
```

---

## Step 4: Documentation Site

```
Create documentation for the design system built in Steps 1-3:

**Doc tool:** {{Storybook | Docusaurus | custom}}

Include:
1. Getting started guide (installation, setup, theming)
2. Design principles and when to use this system
3. Token reference with visual swatches
4. Component catalog with live examples
5. Pattern library (common layouts built from components)
6. Contribution guide for adding new components
7. Changelog / versioning strategy
```

## Usage Notes

- Step 1 (tokens) is the foundation — get stakeholder buy-in before proceeding
- Don't build every component upfront — Step 2 prioritizes the minimum set
- Storybook stories from Step 3 double as visual regression tests
- The documentation site (Step 4) is what makes a design system adoptable

---

# Accessibility Audit Playbook

> Comprehensive a11y review from code analysis to remediation plan.

## When to Use

- Preparing for WCAG compliance
- Reviewing a feature before launch
- Responding to user-reported accessibility issues
- Annual accessibility audit

---

## Step 1: Automated Scan Interpretation

```
Here are the results from an accessibility scan (axe-core / Lighthouse / WAVE):

```
{{SCAN_RESULTS}}
```

For each violation:
1. Explain what it means in plain English
2. Who is affected (screen reader users, keyboard users, low vision, cognitive)
3. WCAG criterion and level (A, AA, AAA)
4. Priority: critical (blocks usage) -> high (major barrier) -> medium -> low
5. How to fix it with specific code examples
6. How to test the fix
```

---

## Step 2: Manual Review

```
Review this page/component code for accessibility issues that automated tools miss:

```{{LANGUAGE}}
{{YOUR_CODE}}
```

Check these categories:
1. **Keyboard navigation** — Can every interactive element be reached and operated with keyboard alone?
2. **Focus management** — Is focus order logical? Is focus trapped in modals? Is focus restored after dialogs close?
3. **Screen reader experience** — Do headings form a logical outline? Are dynamic updates announced? Are decorative images hidden?
4. **Color and contrast** — Does meaning rely solely on color? Are contrast ratios sufficient?
5. **Motion** — Is there a way to reduce/disable animations? Does anything auto-play?
6. **Cognitive** — Are error messages helpful? Are instructions clear? Is the reading level appropriate?
7. **Touch** — Are tap targets large enough? Is there adequate spacing between targets?
8. **Zoom** — Does the layout work at 200% zoom? Does text reflow properly?

For each issue, provide the WCAG success criterion, severity, and a code fix.
```

---

## Step 3: Remediation Plan

```
Based on these accessibility findings:

{{FINDINGS_FROM_STEPS_1_AND_2}}

Create a prioritized remediation plan:

1. **Immediate fixes** (< 1 hour each) — Quick wins that remove critical barriers
2. **Short-term fixes** (1-5 hours each) — Important improvements
3. **Long-term fixes** (requires refactoring) — Structural changes needed

For each fix:
- Specific code change needed
- Estimated effort
- Which user group benefits
- Testing approach (manual + automated)
- Regression prevention (how to keep it from breaking again)

Also recommend:
- Ongoing testing strategy (CI integration, manual testing cadence)
- Screen reader testing protocol (which screen readers, which browsers)
- User testing with assistive technology users
```

## Usage Notes

- Automated scans catch ~30% of issues — Step 2 (manual review) is essential
- Test with actual screen readers (NVDA on Windows, VoiceOver on Mac)
- WCAG AA is the standard target; AAA for government/healthcare

---

# React-Specific Prompts

> Prompts tailored for React development patterns.

---

## Hook Design

```
Design a custom React hook for {{PURPOSE}}:

**Hook name:** use{{NAME}}
**Input parameters:** {{PARAMS}}
**Return value:** {{WHAT_IT_RETURNS}}
**Side effects:** {{EXTERNAL_INTERACTIONS}} (API calls, localStorage, DOM, WebSocket)

Requirements:
1. TypeScript with proper generic types
2. Handle loading, error, and success states
3. Cleanup on unmount (abort controllers, event listeners)
4. Avoid unnecessary re-renders (stable references with useCallback/useMemo)
5. Support React Strict Mode (handle double-mount in dev)
6. Include JSDoc comments

Provide:
- The hook implementation
- Type definitions
- Usage example in a component
- Unit test using React Testing Library
```

---

## State Management Architecture

```
Design the state management approach for this React application:

**App description:** {{WHAT_THE_APP_DOES}}
**Current state tool:** {{NONE | Context | Redux | Zustand | Jotai | other}}
**Pain points:** {{CURRENT_ISSUES}} (e.g., prop drilling, unnecessary re-renders, stale data)

**State categories:**
- Server state: {{WHAT_COMES_FROM_API}}
- UI state: {{LOCAL_COMPONENT_STATE}}
- Form state: {{FORM_DATA}}
- URL state: {{WHAT_LIVES_IN_THE_URL}}

Recommend:
1. Which tool for each state category (and why)
2. State shape / store design
3. How to avoid common pitfalls (over-normalization, stale closures, render waterfalls)
4. Data fetching and caching strategy (React Query, SWR, or manual)
5. Optimistic update patterns for mutations
6. DevTools and debugging approach
```

---

## Performance Optimization

```
This React component/page is slow. Help me optimize it:

```tsx
{{YOUR_CODE}}
```

**Symptoms:** {{WHAT_FEELS_SLOW}} (initial load, re-renders, scroll jank, input lag)
**Component tree depth:** {{APPROXIMATE_DEPTH}}
**Data size:** {{HOW_MUCH_DATA_IS_RENDERED}}

Analyze and fix:
1. **Unnecessary re-renders** — Components re-rendering when they shouldn't
2. **Missing memoization** — Where useMemo, useCallback, React.memo actually help (and where they don't)
3. **Bundle size** — Imports that could be lazy loaded or code-split
4. **Render performance** — Lists that need virtualization, heavy computations in render
5. **Effect waterfalls** — Sequential data fetching that should be parallel
6. **Layout thrashing** — DOM reads/writes that cause forced reflow

Provide the optimized code with before/after React Profiler expectations.
```

---

## Migration Helper (Class -> Hooks)

```
Convert this class component to a functional component with hooks:

```tsx
{{CLASS_COMPONENT_CODE}}
```

Convert:
- this.state -> useState
- componentDidMount/Update/Unmount -> useEffect (with correct deps)
- Class methods -> functions (with useCallback where needed)
- Context consumers -> useContext
- Refs -> useRef
- Error boundaries -> keep as class (or use react-error-boundary library)

Flag any behavioral differences between the class and hook versions.
```

## Usage Notes

- Hook design: always mention cleanup — it's the most commonly missed piece
- State management: the right answer is usually "multiple tools for different state types"
- Performance: profile first with React DevTools — don't optimize blindly
