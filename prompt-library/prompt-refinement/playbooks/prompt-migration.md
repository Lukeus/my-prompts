# Prompt Migration Playbook

> Migrate prompts between models (e.g., GPT-4 → Claude, or across model versions) without quality loss.

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
