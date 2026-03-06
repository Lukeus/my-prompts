# Architecture Design Playbook

> Multi-step workflow for designing a system from requirements to implementation plan.

## When to Use

- Starting a new service or major feature
- Evaluating whether to build vs. buy
- Preparing for a technical design review
- Scaling an existing system that's hitting limits

---

## Step 1: Requirements Clarification

```
I'm designing a system for {{HIGH_LEVEL_DESCRIPTION}}.

Here's what I know:
- **Users:** {{WHO_AND_HOW_MANY}}
- **Core use cases:** {{LIST_MAIN_USER_FLOWS}}
- **Scale:** {{REQUESTS_PER_SECOND | STORAGE_NEEDS | CONCURRENT_USERS}}
- **Latency requirements:** {{P50_AND_P99_TARGETS}}
- **Availability target:** {{UPTIME_SLA}}
- **Budget constraints:** {{IF_ANY}}

Before I design, help me identify:
1. Ambiguous requirements that need clarification
2. Implicit requirements I might be missing (security, compliance, observability)
3. Scale-related requirements I should plan for (10x growth)
4. Non-functional requirements that are easy to forget
5. Questions I should ask stakeholders before proceeding
```

---

## Step 2: Architecture Options

```
Given these requirements for {{SYSTEM_NAME}}:

{{PASTE_REQUIREMENTS_FROM_STEP_1}}

Propose 2-3 architecture options:

For each option, provide:
1. High-level architecture diagram (mermaid)
2. Key technology choices and why
3. How it handles the top 3 use cases
4. Scaling strategy
5. Failure modes and how they're mitigated
6. Estimated development effort
7. Operational complexity (how hard is this to run?)
8. Cost estimate at current and 10x scale

Then recommend one option with clear justification.
```

---

## Step 3: Detailed Design

```
I've chosen {{SELECTED_ARCHITECTURE}} for {{SYSTEM_NAME}}.

Now produce a detailed design:

1. **Component diagram** — All services, databases, queues, caches with their interactions
2. **Data model** — Core entities, relationships, storage decisions
3. **API contracts** — Key interfaces between components
4. **Data flow** — How a request flows through the system for each core use case
5. **Security design** — Auth, encryption, secrets management, network boundaries
6. **Observability** — Metrics, logs, traces, dashboards, alerts
7. **Deployment** — Infrastructure, CI/CD, environments, rollback strategy

For each component, note:
- Build vs. buy decision
- Technology choice with rationale
- Configuration that needs to be environment-specific
```

---

## Step 4: Implementation Plan

```
Given this architecture for {{SYSTEM_NAME}}:

{{SUMMARY_OF_DESIGN}}

Create a phased implementation plan:

Phase 1 (MVP): What's the minimum to ship something useful?
Phase 2: What adds the most value after MVP?
Phase 3: What completes the full vision?

For each phase:
1. Specific deliverables
2. Team size and skills needed
3. Dependencies and blockers
4. Estimated timeline
5. Risks and mitigations
6. Definition of done

Also identify:
- What can be built in parallel
- What should be prototyped/spiked first
- Technical debt that's acceptable in Phase 1 but must be addressed later
```

## Usage Notes

- Step 1 is the most important — don't rush it
- Architecture options (Step 2) prevent anchoring on the first idea
- Share the Step 4 implementation plan with your team for estimation
- Revisit Step 2 if you learn new requirements during detailed design
