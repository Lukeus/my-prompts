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
