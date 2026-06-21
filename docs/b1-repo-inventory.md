# B1 — Repository Inventory

**Target OSS:** [ptrstn/fastapi-sqlalchemy-pytest-example](https://github.com/ptrstn/fastapi-sqlalchemy-pytest-example)  
**Local commit analyzed:** `19047d7` (clone at `~/Desktop/repos/fastapi-sqlalchemy-pytest-example`)

## Purpose

Small FastAPI + SQLModel sample with pytest coverage — CRUD for users and items backed by SQLite.

## Top-level layout

| Path | Role |
|------|------|
| `src/mypackage/` | Application package (models, CRUD, API routers, settings) |
| `tests/` | Pytest suite with shared fixtures |
| `pyproject.toml` | Packaging, runtime deps, pytest env (`.test.env`) |
| `.github/workflows/python-package.yml` | CI workflow |
| `.test.env` | Test database URL override |

## Runtime stack

- **Python** ≥ 3.8 (`pyproject.toml`)
- **FastAPI** HTTP layer
- **SQLModel** ORM (SQLAlchemy + Pydantic)
- **uvicorn** ASGI server (dev)
- **pytest** + **httpx** TestClient for API tests

## Entry points

| Entry | Location |
|-------|----------|
| ASGI app | `src/mypackage/main.py` → `app` |
| API router mount | `src/mypackage/api/v1/router.py` prefix `/api` |
| DB bootstrap | `database.create_db_and_tables()` on lifespan startup |

## Key modules

```
src/mypackage/
├── main.py           # FastAPI app + lifespan
├── models.py         # User, Item SQLModel tables
├── schemas.py        # Pydantic request/response models
├── crud.py           # DB operations
├── database.py       # Engine, session generator, DDL
├── settings.py       # pydantic-settings for DB URL
└── api/v1/
    ├── router.py
    └── endpoints/
        ├── users.py
        └── items.py
```

## Test layout

- `tests/conftest.py` — module-scoped DB create/drop, TestClient fixture
- `tests/test_api.py` — HTTP integration tests
- `tests/test_crud.py`, `test_database.py`, `test_settings.py` — unit-level

## How to run (upstream)

```bash
pip install -e ".[test]"
pytest
uvicorn mypackage.main:app --reload
```

## Method

Inventory derived from directory listing, `pyproject.toml`, and router imports. No application code was modified for B1.
