# Systematic Debugging Playbook

> A structured approach to diagnosing and fixing bugs, from reproduction to root cause to prevention.

## When to Use

- Bug that's hard to reproduce
- Production incident requiring methodical investigation
- Performance regression with unclear cause
- Flaky tests or intermittent failures

---

## Step 1: Bug Characterization

```
Help me systematically debug this issue:

**Symptom:** {{WHAT_IS_HAPPENING}}
**Expected behavior:** {{WHAT_SHOULD_HAPPEN}}
**Environment:** {{WHERE_IT_HAPPENS}} (prod, staging, local, specific OS/browser)
**Frequency:** {{ALWAYS | INTERMITTENT | FIRST_TIME}}
**First noticed:** {{WHEN}}
**Recent changes:** {{WHAT_CHANGED}} (deploys, config changes, data changes, dependency updates)

Error output:
```
{{ERROR_MESSAGES_STACK_TRACES_LOGS}}
```

Based on this, help me:
1. Classify the bug type (logic error, race condition, resource exhaustion, configuration, dependency)
2. Generate 3-5 hypotheses ranked by likelihood
3. For each hypothesis, provide a specific diagnostic step to confirm or rule it out
4. Identify what additional information would narrow it down fastest
```

---

## Step 2: Isolation & Reproduction

```
I'm trying to reproduce this bug:

**Hypothesis:** {{MOST_LIKELY_CAUSE_FROM_STEP_1}}
**System:** {{RELEVANT_ARCHITECTURE}}

Help me create:
1. A minimal reproduction case — smallest possible code/config that triggers the bug
2. Environment setup instructions to match the failing environment
3. A test that currently fails and will pass once the bug is fixed
4. Logging/instrumentation to add if the bug can't be reproduced locally

If this is an intermittent bug, also suggest:
- Race condition detection techniques
- Load/stress test to trigger timing-dependent failures
- State combinations to explore systematically
```

---

## Step 3: Root Cause Analysis

```
I've confirmed the bug is caused by:

**Root cause:** {{WHAT_YOU_FOUND}}
**Evidence:** {{HOW_YOU_CONFIRMED_IT}}

Now help me:
1. Understand why this was possible — what guard was missing?
2. Determine the blast radius — what else might be affected by the same root cause?
3. Design the fix with the smallest possible change
4. Identify regression tests to prevent recurrence
5. Write a brief post-mortem summary:
   - Timeline
   - Impact
   - Root cause
   - Fix
   - Follow-up actions to prevent similar issues
```

## Usage Notes

- Resist the urge to jump to Step 3 — Step 1's hypothesis ranking saves time
- "What changed recently" is the single most useful diagnostic question
- The post-mortem in Step 3 is invaluable for team learning — don't skip it
- For production incidents, add timestamps to everything
