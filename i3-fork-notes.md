# I3 — Small Safe Change

Two artifacts demonstrate I3:

## 1. In-monorepo implementation

**Path:** `exercises/i3-mini-change/`

Added pagination (`skip`, `limit`) to GET `/notes` on a seeded mini-app.

```bash
cd exercises/i3-mini-change
pip install -r requirements.txt
pytest tests/ -v
```

## 2. OSS fork

**Upstream:** https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example  
**Fork branch:** https://github.com/t-atul1s/fastapi-sqlalchemy-pytest-example/tree/feature/get-user-by-id

Change: `GET /api/users/{user_id}` with tests (31-line diff, 3 files).

## Risk assessment

| Risk | Mitigation |
|------|------------|
| Breaking existing routes | Read-only new route |
| Test regression | Ran full pytest suite |
| Data migration | None required |

## Why two artifacts?

The monorepo includes a self-contained demo for one-command verification. The fork link documents the upstream OSS change with full git history.
