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
