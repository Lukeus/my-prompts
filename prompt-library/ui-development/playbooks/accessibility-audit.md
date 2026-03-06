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
