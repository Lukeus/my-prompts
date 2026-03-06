# Prompt Library

A curated collection of prompts for data engineering, software development, UI development, prompt refinement, and codebase research.

## Structure

```
prompt-library/
├── data-engineering/
│   ├── templates/        # Quick fill-in-the-blank prompts
│   ├── playbooks/        # Deep, detailed prompt workflows
│   └── stack-specific/   # dbt, Airflow, Spark, etc.
├── software-development/
│   ├── templates/
│   ├── playbooks/
│   └── stack-specific/   # Python, Go, Rust, etc.
├── ui-development/
│   ├── templates/
│   ├── playbooks/
│   └── stack-specific/   # React, Vue, Svelte, etc.
├── prompt-refinement/
│   ├── templates/
│   └── playbooks/
├── codebase-research/
│   ├── exploration/      # Understanding unfamiliar repos
│   ├── documentation/    # Generating docs from code
│   └── stack-specific/
└── README.md
```

## How to Use

**Templates** — Copy, fill in the `{{placeholders}}`, and go. Best for quick tasks.

**Playbooks** — Step-by-step workflows with context-setting, chain-of-thought guidance, and example outputs. Use when you need depth.

**Stack-specific** — Variants tailored to particular tools and frameworks. Extend or modify as your stack evolves.

## Conventions

- `{{PLACEHOLDER}}` — Replace with your specific context
- `[OPTIONAL]` — Include or remove based on your needs
- Prompts are written to work with Claude, GPT-4, and other capable LLMs
- Each file includes a brief description, the prompt itself, and usage notes
