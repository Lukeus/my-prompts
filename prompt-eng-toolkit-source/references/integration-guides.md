# AI Tool Integration Guides

How to install and configure the prompt toolkit for each AI coding assistant.

---

## Claude Code (.claude/)

### Setup

```
your-repo/
├── .claude/
│   └── prompts/
│       ├── README.md
│       ├── INDEX.md
│       ├── _project-profile.yml
│       ├── data-engineering/
│       ├── software-development/
│       ├── ui-development/
│       ├── prompt-refinement/
│       └── codebase-research/
└── CLAUDE.md  ← optional: add a line referencing the prompts
```

### CLAUDE.md Integration

If the project has a `CLAUDE.md`, add this section:

```markdown
## Prompt Library

This project includes an adapted prompt library in `.claude/prompts/`.
When asked to review code, debug, design, or document — check for a
relevant prompt template first.

Key prompts:
- Code review: `.claude/prompts/software-development/templates/code-review.md`
- Debugging: `.claude/prompts/software-development/playbooks/debugging-playbook.md`
- Documentation: `.claude/prompts/codebase-research/documentation/`
```

### How Claude Uses These

Claude Code automatically sees files in `.claude/` as project context. When a developer asks for help with a task that matches a prompt template, Claude can reference the pre-adapted template to produce better, more consistent results.

---

## GitHub Copilot (.github/copilot/)

### Setup

```
your-repo/
├── .github/
│   └── copilot/
│       └── prompts/
│           ├── README.md
│           ├── INDEX.md
│           ├── _project-profile.yml
│           ├── data-engineering/
│           ├── software-development/
│           ├── ui-development/
│           ├── prompt-refinement/
│           └── codebase-research/
```

### copilot-instructions.md Integration

If the project has `.github/copilot-instructions.md`, add:

```markdown
## Prompt Templates

This repo includes adapted prompt templates in `.github/copilot/prompts/`.
Reference them when reviewing code, designing APIs, debugging, or generating docs.
Check the INDEX.md for a full catalog of available prompts.
```

### How Copilot Uses These

In Copilot Chat, users can reference prompts with `@workspace`:
- `@workspace Use the code review prompt to review this PR`
- `@workspace Follow the debugging playbook for this error`

---

## Cursor (.cursor/)

### Setup

```
your-repo/
├── .cursor/
│   └── prompts/
│       ├── README.md
│       ├── INDEX.md
│       ├── _project-profile.yml
│       ├── data-engineering/
│       ├── software-development/
│       ├── ui-development/
│       ├── prompt-refinement/
│       └── codebase-research/
```

### .cursorrules Integration

If the project has `.cursorrules`, add:

```
When asked to review code, debug issues, design APIs, or generate docs,
check .cursor/prompts/ for adapted prompt templates that match the task.
Use the pre-filled project context from those templates.
```

### How Cursor Uses These

Cursor reads `.cursor/` for project rules and context. The prompts become part of the project's AI configuration, helping Cursor produce more consistent, project-aware responses.

---

## Generic / Tool-Agnostic

### Setup

```
your-repo/
├── docs/
│   └── prompts/
│       ├── README.md
│       ├── INDEX.md
│       ├── _project-profile.yml
│       └── ... (all categories)
```

Or use `.ai/prompts/` as a vendor-neutral convention.

### How Teams Use These

1. Developers browse `INDEX.md` to find the right prompt
2. Copy the prompt template
3. Fill in task-specific details
4. Paste into whatever AI tool they're using

This approach works with any LLM — Claude, GPT, Gemini, Llama, or local models.

---

## Version Control Recommendations

**Commit the prompts.** They're project documentation, not secrets.

```gitignore
# DON'T ignore prompts — they should be versioned
# .claude/prompts/  ← don't add this to .gitignore
```

**Review prompt changes.** When someone modifies a prompt, review it like code — it affects how AI interacts with your project.

**Re-adapt on major changes.** After framework upgrades, database migrations, or architecture changes, re-run the scan to keep prompts current.
