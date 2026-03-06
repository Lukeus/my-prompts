# Legacy Code Analysis Prompts

> Specialized prompts for understanding and safely modifying legacy codebases.

---

## Legacy Code Archaeology

```
I'm working with a legacy codebase that has limited documentation. Help me understand it:

**Language:** {{LANGUAGE}}
**Approximate age:** {{YEARS}}
**Original framework/version:** {{IF_KNOWN}}
**What this system does:** {{BUSINESS_PURPOSE}}

**Sample code (representative section):**
```{{LANGUAGE}}
{{CODE_SAMPLE}}
```

Analyze:
1. **Historical context** — What era of {{LANGUAGE}} development does this code reflect? What conventions were common then?
2. **Implicit patterns** — What design patterns are being used, even if named/implemented differently than modern versions?
3. **Hidden business logic** — What business rules are embedded in the code? (Often the most valuable undocumented knowledge)
4. **Technical debt inventory** — Categorize the debt:
   - Intentional (shortcuts that were known tradeoffs)
   - Accidental (code that drifted from its original design)
   - Environmental (outdated patterns that were best practice at the time)
5. **Risk map** — Which parts are most fragile? Where would a change most likely break things?
6. **Modernization priority** — If you could only modernize 3 things, what would have the biggest impact?
```

---

## Safe Modification Guide

```
I need to modify this legacy code but I'm afraid of breaking things:

**Code to modify:**
```{{LANGUAGE}}
{{LEGACY_CODE}}
```

**Change needed:** {{WHAT_I_NEED_TO_DO}}
**Test coverage:** {{NONE | MINIMAL | MODERATE | GOOD}}
**Can I add tests?** {{YES | NO_BECAUSE}}

Help me make this change safely:
1. **Characterization tests** — If no tests exist, what tests should I write first to capture current behavior (even if the behavior is "wrong")?
2. **Seams** — Where can I insert a change without modifying existing code? (dependency injection points, interfaces, configuration)
3. **Strangler fig approach** — Can I wrap the old code and gradually redirect?
4. **Minimal change** — What's the smallest possible modification to achieve the goal?
5. **Rollback plan** — If the change causes issues, how do I revert safely?
6. **Verification** — How do I confirm the change works without comprehensive tests?
```

## Usage Notes

- "Hidden business logic" findings should be documented immediately — this knowledge is perishable
- Characterization tests are the key to safely modifying legacy code
- The strangler fig pattern avoids big-bang rewrites — prefer it when possible
- Respect the legacy code — it's running in production for a reason
