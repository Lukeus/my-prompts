# Prompt Engineering Workflow Playbook

> End-to-end process for developing, testing, and iterating on prompts for production use.

## When to Use

- Building a prompt for a product feature or automated workflow
- Prompt is giving inconsistent or unsatisfactory results
- Migrating a prompt from one model to another
- Optimizing for cost (token reduction) without quality loss

---

## Step 1: Requirements & Constraints

```
I'm building a prompt for the following use case:

**Purpose:** {{WHAT_THE_PROMPT_DOES}}
**Integration:** {{WHERE_IT_RUNS}} (e.g., API call, chatbot, agent, batch processing)
**Model:** {{TARGET_MODEL}}
**Token budget:** {{MAX_INPUT_TOKENS}} input / {{MAX_OUTPUT_TOKENS}} output
**Latency requirement:** {{MAX_ACCEPTABLE_LATENCY}}
**Cost sensitivity:** {{HIGH | MEDIUM | LOW}}

**Input characteristics:**
- Source: {{WHERE_INPUT_COMES_FROM}}
- Format: {{STRUCTURED | UNSTRUCTURED | MIXED}}
- Length range: {{MIN_TO_MAX}}
- Language: {{LANGUAGES}}

**Output requirements:**
- Format: {{JSON | MARKDOWN | PLAIN_TEXT | STRUCTURED}}
- Must include: {{REQUIRED_FIELDS}}
- Must NOT include: {{FORBIDDEN_CONTENT}}
- Consistency: {{HOW_SIMILAR_SHOULD_OUTPUTS_BE_FOR_SIMILAR_INPUTS}}

List the requirements I might be missing and suggest constraints I should add.
```

---

## Step 2: Draft & Structure

```
Based on these requirements:

{{REQUIREMENTS_FROM_STEP_1}}

Draft the prompt using this structure:
1. **Role/persona** — Who the model should act as
2. **Context** — Background information needed for the task
3. **Task** — Clear, specific instructions
4. **Constraints** — Boundaries and rules
5. **Output format** — Exact schema or template
6. **Examples** — 2-3 few-shot examples (input -> output pairs)
7. **Edge case handling** — What to do when uncertain

Provide two versions:
- **Verbose version** — Maximum clarity, best quality, higher token cost
- **Compact version** — Minimal tokens, same core behavior

Estimate token count for each version.
```

---

## Step 3: Test & Iterate

```
Here's my current prompt:

```
{{YOUR_PROMPT}}
```

And here are the results from testing:

| Test Case | Input | Expected Output | Actual Output | Pass/Fail |
|-----------|-------|-----------------|---------------|-----------|
| {{CASE_1}} | {{INPUT}} | {{EXPECTED}} | {{ACTUAL}} | {{P/F}} |
| {{CASE_2}} | ... | ... | ... | ... |

Analyze the failures and suggest targeted prompt modifications:
1. What pattern do the failures share?
2. What instruction is the model misinterpreting?
3. Provide a specific prompt edit to fix each failure type
4. Will the fix affect any passing test cases? (regression risk)
5. Suggest additional test cases to verify the fix
```

---

## Step 4: Production Hardening

```
My prompt is working well in testing. Help me prepare it for production:

```
{{YOUR_PROMPT}}
```

**Production environment:** {{API | CHATBOT | AGENT | BATCH}}

Harden it by:
1. **Input sanitization** — Handle malformed, adversarial, or injection-style inputs
2. **Output validation** — Define a schema to validate responses programmatically
3. **Fallback behavior** — What should happen if the model fails or gives a malformed response
4. **Token optimization** — Reduce token count without quality loss
5. **Version tagging** — Add a version identifier for A/B testing and rollback
6. **Monitoring hooks** — What to log for quality monitoring in production
7. **Model migration notes** — What might break if you switch models later
```

## Usage Notes

- Don't skip Step 1 — vague requirements lead to endless iteration
- Step 3 is iterative — expect 3-5 rounds of test -> fix -> retest
- The compact version from Step 2 often works fine — try it first to save cost
- Version tagging (Step 4) is essential for debugging production issues
