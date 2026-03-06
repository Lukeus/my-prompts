# Docker & DevOps Prompts

> Prompts for containerization, CI/CD, and infrastructure.

---

## Dockerfile Optimization

```
Optimize this Dockerfile for {{GOAL}} (e.g., smaller image size, faster builds, security):

```dockerfile
{{YOUR_DOCKERFILE}}
```

**Application type:** {{TYPE}} (e.g., Python API, Node.js app, Go binary)
**Current image size:** {{SIZE}}
**Build time:** {{DURATION}}

Provide:
1. Optimized Dockerfile with comments explaining each improvement
2. Multi-stage build if applicable
3. Layer caching strategy for fastest rebuilds
4. Security hardening (non-root user, minimal base image, no secrets in layers)
5. .dockerignore recommendations
6. Before/after comparison of image size and build time
```

---

## CI/CD Pipeline Design

```
Design a CI/CD pipeline for the following project:

**Repository:** {{MONO_OR_MULTI_REPO}}
**Language(s):** {{LANGUAGES}}
**Platform:** {{GitHub Actions | GitLab CI | Jenkins | CircleCI}}
**Deployment target:** {{AWS | GCP | Azure | K8s | bare metal}}
**Environments:** {{dev | staging | prod}}

The pipeline should include:
1. Code quality gates (lint, format, type check)
2. Test stages (unit → integration → e2e)
3. Security scanning (SAST, dependency audit, container scan)
4. Build and push artifacts/images
5. Deployment with rollback capability
6. Environment promotion workflow
7. Notification hooks (Slack, email)

Provide the complete pipeline YAML/config with comments.
```

---

## Infrastructure as Code

```
Write {{TOOL}} (e.g., Terraform, Pulumi, CDK) code for:

**Infrastructure:** {{WHAT_TO_PROVISION}}
**Cloud provider:** {{AWS | GCP | Azure}}
**Environment strategy:** {{HOW_ENVS_ARE_SEPARATED}} (e.g., separate accounts, namespaces, workspaces)

Requirements:
- Modular and reusable (use modules/constructs)
- Environment-specific variables with sensible defaults
- State management configuration
- Tagging strategy for cost tracking
- Security best practices (least privilege IAM, encryption at rest)
- Output the important values (endpoints, IDs) for downstream use
```

## Usage Notes

- Always include the current Dockerfile when optimizing — context matters
- For CI/CD, mention if you use monorepo tooling (Nx, Turborepo, Bazel)
- IaC prompts work best when you specify the exact cloud services needed
