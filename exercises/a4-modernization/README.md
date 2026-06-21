# A4 — Modernization

Refactored legacy dict/list helpers to typed dataclasses.

## Changes

| Before | After |
|--------|-------|
| `has_key` + index loops | membership + list comprehension |
| untyped dicts | `@dataclass(frozen=True) User` |
| manual search loop | `next(..., None)` |

## Verify

```bash
PYTHONPATH=modernized pytest tests/ -v
```
