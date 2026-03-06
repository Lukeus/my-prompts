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
