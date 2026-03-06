# Auto Wiki Generator (DeepWiki-Style)

> Generate comprehensive wiki-style documentation from a codebase, similar to DeepWiki.

## Prompt — Full Wiki Generation

```
Generate a comprehensive wiki for this codebase:

**Repository:** {{REPO_NAME}}
**Language(s):** {{LANGUAGES}}
**Directory structure:**
```
{{TREE_OUTPUT}}
```

**Key source files:**
```{{LANGUAGE}}
{{PASTE_KEY_FILES_OR_SUMMARIES}}
```

Generate a wiki with these sections:

## 1. Project Overview
- What the project does (inferred from code, README, comments)
- Key features and capabilities
- Target users / use cases

## 2. Architecture
- System architecture diagram (mermaid)
- Component breakdown with responsibilities
- Data flow diagrams for core use cases
- Technology stack and why each piece was chosen (inferred)

## 3. Module Reference
For each major module/package:
- Purpose and responsibility
- Public API / exports
- Dependencies (what it imports)
- Key classes/functions with brief descriptions
- Configuration it reads

## 4. Data Model
- Entity relationship diagram (mermaid)
- Table/collection descriptions
- Key relationships and constraints
- Data flow from input to storage

## 5. API Reference (if applicable)
- All endpoints with methods, params, and response shapes
- Authentication requirements
- Rate limits and pagination
- Error response format

## 6. Configuration Guide
- All environment variables with descriptions and defaults
- Feature flags
- Configuration files and their schema

## 7. Development Guide
- Local setup instructions
- How to run tests
- How to add a new feature (following existing patterns)
- Coding conventions and style guide (inferred from code)

## 8. Glossary
- Domain-specific terms used in the codebase
- Abbreviations and acronyms

Format each section with clear headings, code examples from the actual codebase, and cross-references between sections.
```

## Usage Notes

- For large repos, generate the wiki module-by-module rather than all at once
- Feed in the most important 10-15 files plus the directory tree
- The "inferred" sections are the most valuable — they extract undocumented knowledge
- Update the wiki whenever the architecture changes significantly
