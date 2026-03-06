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
