# Prompt Refinement Reference

## Table of Contents

1. [Prompt Improver Template](#prompt-improver-template)
2. [System Prompt Generator Template](#system-prompt-generator-template)
3. [Chain-of-Thought Prompt Designer](#chain-of-thought-prompt-designer)
4. [Evaluation Test Generator](#evaluation-test-generator)
5. [Prompt Engineering Workflow Playbook](#prompt-engineering-workflow-playbook)
6. [Prompt Migration Playbook](#prompt-migration-playbook)

---

# Prompt Improver Template

> Take a rough prompt and make it production-quality.

## Prompt

```
Improve the following prompt for better, more consistent results:

**Original prompt:**
```
{{YOUR_PROMPT}}
```

**What I'm trying to achieve:** {{GOAL}}
**LLM I'm using this with:** {{MODEL}} (e.g., Claude, GPT-4, Llama)
**What's wrong with the current output:** {{ISSUES}} (e.g., too vague, inconsistent format, misses edge cases)

Improve it by:
1. Adding clear structure (role, context, task, constraints, output format)
2. Making ambiguous instructions specific and measurable
3. Adding examples of good and bad outputs (few-shot)
4. Specifying the output format explicitly
5. Adding edge case handling instructions
6. Removing unnecessary verbosity that wastes tokens

Provide:
- The improved prompt
- Explanation of each change and why it helps
- 2-3 test cases to verify the improved prompt works
```

## Usage Notes

- Include example outputs (good and bad) when describing issues
- Specify the model — prompting strategies differ between Claude and GPT
- Test the improved prompt with edge cases before deploying

---

# System Prompt Generator Template

> Create a system prompt for an AI assistant with a specific role.

## Prompt

```
Create a system prompt for an AI assistant with the following role:

**Role:** {{ROLE}} (e.g., senior code reviewer, technical writer, data analyst)
**Audience:** {{WHO_WILL_INTERACT}} (e.g., junior developers, non-technical stakeholders)
**Domain:** {{SPECIFIC_DOMAIN}} (e.g., fintech, healthcare, e-commerce)
**Tone:** {{TONE}} (e.g., professional, friendly, concise, Socratic)

The assistant should:
- {{BEHAVIOR_1}} (e.g., always ask clarifying questions before answering)
- {{BEHAVIOR_2}} (e.g., cite sources when making claims)
- {{BEHAVIOR_3}} (e.g., provide examples with every explanation)

The assistant should NOT:
- {{ANTI_BEHAVIOR_1}} (e.g., make assumptions about the user's skill level)
- {{ANTI_BEHAVIOR_2}} (e.g., provide code without explaining it)

**Output constraints:**
- Default response length: {{LENGTH}}
- Format preferences: {{FORMAT}}
- Language/terminology level: {{LEVEL}}

Generate a complete system prompt that:
1. Defines the role and expertise clearly
2. Sets behavioral guidelines with examples
3. Specifies output format defaults
4. Includes guardrails (what to do when uncertain)
5. Handles edge cases (off-topic questions, unclear requests)
```

## Usage Notes

- The "should NOT" section is as important as the "should" section
- Test with adversarial inputs (off-topic, ambiguous, contradictory requests)
- Keep system prompts under 2000 tokens for best results on most models

---

# Chain-of-Thought Prompt Designer

> Build prompts that guide the LLM through structured reasoning.

## Prompt

```
Design a chain-of-thought prompt for the following task:

**Task:** {{TASK_DESCRIPTION}}
**Input:** {{WHAT_THE_USER_PROVIDES}}
**Expected output:** {{WHAT_THE_LLM_SHOULD_PRODUCE}}
**Common failure modes:** {{WHERE_SIMPLE_PROMPTS_GO_WRONG}}

Build a prompt that forces step-by-step reasoning:
1. Define explicit thinking steps the model must follow
2. Use structured output tags (e.g., <analysis>, <reasoning>, <conclusion>)
3. Include a self-check step ("verify your answer by...")
4. Add at least one worked example showing the full chain of thought
5. Specify when the model should say "I'm not sure" vs. give a best guess

The prompt should prevent these common CoT failures:
- Skipping steps when the answer seems obvious
- Anchoring on the first hypothesis
- Losing track of constraints mid-reasoning
- Providing a confident answer despite weak reasoning
```

## Usage Notes

- CoT is most valuable for multi-step reasoning, math, and logic tasks
- For simple tasks, CoT adds unnecessary tokens — use direct prompts instead
- The self-check step catches ~20% of errors the model would otherwise make
- Test with cases where the intuitive answer is wrong — that's where CoT shines

---

# Evaluation Test Generator

> Create test cases to measure prompt quality before deploying.

## Prompt

```
Generate evaluation test cases for this prompt:

**Prompt being tested:**
```
{{YOUR_PROMPT}}
```

**What "good" looks like:** {{CRITERIA_FOR_SUCCESS}}
**What "bad" looks like:** {{COMMON_FAILURES}}

Generate test cases in these categories:

1. **Happy path** (5 cases) — Standard inputs that should produce ideal outputs
2. **Edge cases** (5 cases) — Unusual but valid inputs (empty, very long, special characters, multilingual)
3. **Adversarial** (3 cases) — Inputs designed to break the prompt or produce bad output
4. **Ambiguous** (3 cases) — Inputs where the correct behavior isn't obvious

For each test case, provide:
- Input
- Expected output (or acceptable output range)
- What specifically to check (format, accuracy, completeness, tone)
- Pass/fail criteria

Also suggest:
- Automated checks that can be scripted (regex, JSON schema, keyword presence)
- Checks that require human judgment (quality, helpfulness, appropriateness)
```

## Usage Notes

- Run evals before and after every prompt change
- Adversarial cases are the highest-signal tests — don't skip them
- Automate what you can, but budget time for human review of edge cases
- Track eval scores over time to catch regressions

---

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

---

# Prompt Migration Playbook

> Migrate prompts between models (e.g., GPT-4 -> Claude, or across model versions) without quality loss.

## When to Use

- Switching AI providers
- Upgrading to a newer model version
- Optimizing cost by moving to a smaller model
- Comparing models for a specific use case

---

## Step 1: Baseline Capture

```
I'm migrating this prompt from {{SOURCE_MODEL}} to {{TARGET_MODEL}}:

```
{{YOUR_PROMPT}}
```

First, help me create a quality baseline:
1. Identify the prompt techniques that are model-specific:
   - System prompt format/placement
   - Persona/role instructions
   - Output format enforcement (JSON mode, tool use, etc.)
   - Chain-of-thought triggers
   - Token usage patterns
2. Generate 10 diverse test inputs that cover the full capability range
3. Document the expected output quality for each test input
4. Note any model-specific features being used (function calling, vision, etc.)
```

---

## Step 2: Adaptation

```
Adapt this prompt from {{SOURCE_MODEL}} to {{TARGET_MODEL}}:

**Original prompt:**
```
{{PROMPT}}
```

**Known differences between models:**
- {{SOURCE_MODEL}} strengths: {{STRENGTHS}}
- {{TARGET_MODEL}} strengths: {{STRENGTHS}}
- Key behavioral differences: {{DIFFERENCES}}

Adapt by:
1. Adjust formatting to match target model's preferred prompt structure
2. Rephrase instructions that rely on source model's specific behaviors
3. Update system prompt placement and format
4. Adjust example count (some models need more/fewer few-shot examples)
5. Modify output format instructions for target model's tendencies
6. Add guardrails for known target model weaknesses

Provide the adapted prompt and a change log explaining each modification.
```

---

## Step 3: Validation

```
I've migrated a prompt to {{TARGET_MODEL}}. Here are the comparison results:

| Test Case | Source Model Output | Target Model Output | Quality Comparison |
|-----------|--------------------|--------------------|-------------------|
| {{CASE}} | {{OUTPUT}} | {{OUTPUT}} | {{BETTER/SAME/WORSE}} |

For any regressions:
1. Root cause — is it a prompt issue or a model capability gap?
2. If prompt issue: specific fix to try
3. If model gap: workaround or acceptance criteria adjustment
4. Re-test plan after fixes

Final deliverable: migration sign-off checklist.
```

## Usage Notes

- Always baseline before migrating — you can't measure regression without it
- Claude and GPT respond differently to the same prompt — adaptation is always needed
- Smaller models often need more explicit instructions and examples
- Some tasks may genuinely work better on one model — that's useful to know
