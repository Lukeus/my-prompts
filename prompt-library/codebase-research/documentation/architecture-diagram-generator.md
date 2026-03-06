# Architecture Diagram Generator

> Generate visual architecture diagrams from code analysis.

## Prompt

```
Generate architecture diagrams for this codebase:

**Repository structure:**
```
{{TREE_OUTPUT}}
```

**Key configuration files:**
```
{{DOCKER_COMPOSE_OR_K8S_MANIFESTS_OR_INFRA_CONFIG}}
```

**Import/dependency graph (sample):**
```
{{IMPORTS_FROM_KEY_FILES}}
```

Generate the following diagrams in Mermaid syntax:

### 1. System Context Diagram (C4 Level 1)
- The system as a box
- All external actors (users, external services, third-party APIs)
- Relationships between them

### 2. Container Diagram (C4 Level 2)
- Each deployable unit (web app, API, database, queue, cache)
- Technology choices labeled
- Communication protocols between containers

### 3. Component Diagram (C4 Level 3)
- Major components within the primary service
- Their responsibilities and interactions
- Data stores they use

### 4. Data Flow Diagram
- For the top 3 most important use cases:
  - Step-by-step data flow from user action to response
  - Which components are involved at each step
  - Where data is transformed or persisted

### 5. Deployment Diagram
- Infrastructure layout (inferred from config files)
- Environments (dev, staging, prod)
- Networking boundaries

For each diagram:
- Use clear, descriptive labels
- Color-code by type (service=blue, database=green, external=gray)
- Add a brief text description explaining the diagram
```

## Usage Notes

- Docker Compose files are the single best input for container diagrams
- Kubernetes manifests reveal the deployment architecture
- If you don't have infra config, the code's import graph still enables component diagrams
- C4 model levels provide a natural zoom hierarchy — start at Level 1
