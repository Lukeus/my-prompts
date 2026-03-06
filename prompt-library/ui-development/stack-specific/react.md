# React-Specific Prompts

> Prompts tailored for React development patterns.

---

## Hook Design

```
Design a custom React hook for {{PURPOSE}}:

**Hook name:** use{{NAME}}
**Input parameters:** {{PARAMS}}
**Return value:** {{WHAT_IT_RETURNS}}
**Side effects:** {{EXTERNAL_INTERACTIONS}} (API calls, localStorage, DOM, WebSocket)

Requirements:
1. TypeScript with proper generic types
2. Handle loading, error, and success states
3. Cleanup on unmount (abort controllers, event listeners)
4. Avoid unnecessary re-renders (stable references with useCallback/useMemo)
5. Support React Strict Mode (handle double-mount in dev)
6. Include JSDoc comments

Provide:
- The hook implementation
- Type definitions
- Usage example in a component
- Unit test using React Testing Library
```

---

## State Management Architecture

```
Design the state management approach for this React application:

**App description:** {{WHAT_THE_APP_DOES}}
**Current state tool:** {{NONE | Context | Redux | Zustand | Jotai | other}}
**Pain points:** {{CURRENT_ISSUES}} (e.g., prop drilling, unnecessary re-renders, stale data)

**State categories:**
- Server state: {{WHAT_COMES_FROM_API}}
- UI state: {{LOCAL_COMPONENT_STATE}}
- Form state: {{FORM_DATA}}
- URL state: {{WHAT_LIVES_IN_THE_URL}}

Recommend:
1. Which tool for each state category (and why)
2. State shape / store design
3. How to avoid common pitfalls (over-normalization, stale closures, render waterfalls)
4. Data fetching and caching strategy (React Query, SWR, or manual)
5. Optimistic update patterns for mutations
6. DevTools and debugging approach
```

---

## Performance Optimization

```
This React component/page is slow. Help me optimize it:

```tsx
{{YOUR_CODE}}
```

**Symptoms:** {{WHAT_FEELS_SLOW}} (initial load, re-renders, scroll jank, input lag)
**Component tree depth:** {{APPROXIMATE_DEPTH}}
**Data size:** {{HOW_MUCH_DATA_IS_RENDERED}}

Analyze and fix:
1. **Unnecessary re-renders** — Components re-rendering when they shouldn't
2. **Missing memoization** — Where useMemo, useCallback, React.memo actually help (and where they don't)
3. **Bundle size** — Imports that could be lazy loaded or code-split
4. **Render performance** — Lists that need virtualization, heavy computations in render
5. **Effect waterfalls** — Sequential data fetching that should be parallel
6. **Layout thrashing** — DOM reads/writes that cause forced reflow

Provide the optimized code with before/after React Profiler expectations.
```

---

## Migration Helper (Class -> Hooks)

```
Convert this class component to a functional component with hooks:

```tsx
{{CLASS_COMPONENT_CODE}}
```

Convert:
- this.state -> useState
- componentDidMount/Update/Unmount -> useEffect (with correct deps)
- Class methods -> functions (with useCallback where needed)
- Context consumers -> useContext
- Refs -> useRef
- Error boundaries -> keep as class (or use react-error-boundary library)

Flag any behavioral differences between the class and hook versions.
```

## Usage Notes

- Hook design: always mention cleanup — it's the most commonly missed piece
- State management: the right answer is usually "multiple tools for different state types"
- Performance: profile first with React DevTools — don't optimize blindly
