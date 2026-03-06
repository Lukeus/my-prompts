# Prompt Engineering Toolkit

> Auto-adapted prompt library for **{{PROJECT_NAME}}** — generated {{DATE}}

## What's Here

This directory contains {{PROMPT_COUNT}} prompt templates and playbooks, customized for this project's tech stack:

{{STACK_SUMMARY}}

Each prompt has project-specific values pre-filled. You just add the details of your current task and go.

{{TOOL_NOTE}}

## Quick Start

### With Claude Code

```bash
# The prompts are already in .claude/prompts/ — Claude sees them automatically.
# Just ask:
claude "Review this PR using the code review prompt"
claude "Help me debug this failing pipeline"
claude "Generate API docs for the /users routes"
```

### With GitHub Copilot

```bash
# Prompts live in .github/copilot/prompts/
# Reference them in Copilot Chat:
@workspace Use the code review prompt on this file
@workspace Help me design a data pipeline using the pipeline template
```

### With Cursor

```bash
# Prompts are in .cursor/prompts/
# They're available as rules and context in Cursor Chat.
```

### Manual Use (Any LLM)

1. Open the prompt file for what you need
2. Copy the prompt block (the part inside ``` markers)
3. Fill in any remaining `{{PLACEHOLDERS}}`
4. Paste into your AI assistant

## Directory Structure

```
{{DIRECTORY_TREE}}
```

## Keeping Prompts Updated

These prompts were auto-adapted on **{{DATE}}**. If your stack changes (new framework, new database, major refactor), re-adapt:

> "Scan the codebase and re-adapt the prompts in {{PROMPT_DIR}}"

The scan detects what changed and updates only the affected prompts, preserving any manual edits you've made to task-specific placeholders.

## Customizing

These prompts are starting points. Feel free to:

- **Edit placeholders** — swap defaults for your team's conventions
- **Add prompts** — follow the same `{{PLACEHOLDER}}` format
- **Remove categories** — delete directories you don't use
- **Add to version control** — these are meant to be committed and shared

## Categories

### Templates (Quick Use)
Fill-in-the-blank prompts for common tasks. Copy, customize, go.

### Playbooks (Deep Workflows)
Multi-step prompt sequences for complex work like migrations, architecture design, or comprehensive audits. Use when you need depth.

### Stack-Specific
Prompts tailored to your specific tools and frameworks. These have the most project-specific adaptation.
