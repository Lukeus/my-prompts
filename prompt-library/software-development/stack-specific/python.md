# Python-Specific Prompts

> Prompts tailored for Python development best practices.

---

## Project Scaffolding

```
Scaffold a Python project with the following specs:

**Project type:** {{TYPE}} (e.g., CLI tool, REST API, library/package, ETL script, ML pipeline)
**Python version:** {{VERSION}} (e.g., 3.11+)
**Package manager:** {{pip | poetry | uv | pdm}}
**Key dependencies:** {{LIST_MAIN_LIBRARIES}}

Generate:
1. Directory structure following Python packaging best practices
2. pyproject.toml with all config (no setup.py)
3. Makefile or justfile with common commands (test, lint, format, run)
4. Pre-commit config with ruff, mypy, and black/ruff-format
5. GitHub Actions CI workflow
6. Dockerfile (if applicable)
7. Example module with type hints demonstrating the project pattern
8. Corresponding test file with pytest fixtures
```

---

## Type Annotation Retrofit

```
Add comprehensive type annotations to this Python code:

```python
{{YOUR_CODE}}
```

Requirements:
- Use modern Python typing (3.10+ syntax: X | Y instead of Union[X, Y])
- Add return types to all functions
- Type all function parameters
- Use TypedDict for complex dict structures
- Use Protocol for duck typing where appropriate
- Add Generic types where it improves reusability
- Flag any places where the types reveal potential bugs
- Ensure mypy --strict would pass
```

---

## Async Conversion

```
Convert this synchronous Python code to async:

```python
{{YOUR_CODE}}
```

**Async framework:** {{asyncio | trio | anyio}}
**I/O libraries to convert:** {{requests→httpx | psycopg2→asyncpg | etc.}}

Provide:
1. Async version with proper await points
2. Explanation of concurrency opportunities (what can run in parallel)
3. Connection pool / session management for async
4. Error handling adjustments needed for async context
5. Performance comparison notes (when async helps vs. doesn't)
```

---

## Performance Profiling Guide

```
This Python code is too slow. Help me profile and optimize it:

```python
{{YOUR_CODE}}
```

**Current performance:** {{METRIC}} (e.g., "takes 45s for 1M rows")
**Target performance:** {{TARGET}}

Walk me through:
1. Which profiling tool to use (cProfile, line_profiler, memory_profiler, py-spy)
2. The exact commands to run the profiler
3. How to interpret the output
4. Top 3 most likely bottlenecks based on code inspection
5. Optimization strategies for each bottleneck:
   - Algorithm improvements
   - Data structure changes
   - Caching opportunities
   - Vectorization with numpy/pandas
   - Parallelization with multiprocessing/concurrent.futures
```

## Usage Notes

- Project scaffolding: specify your org's conventions if they differ from defaults
- Type annotations: feed modules one at a time for best results
- Async: not everything benefits from async — the prompt helps identify where it matters
