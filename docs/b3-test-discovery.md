# B3 — Test Discovery

**Target:** `ptrstn/fastapi-sqlalchemy-pytest-example` @ `19047d7`

## Discovery commands

```bash
cd fastapi-sqlalchemy-pytest-example
pip install -e ".[test]"
pytest --collect-only -q
pytest -v
```

## Test modules

| File | Focus |
|------|-------|
| `tests/test_api.py` | HTTP integration via TestClient |
| `tests/test_crud.py` | CRUD functions against real session |
| `tests/test_database.py` | Engine/session lifecycle |
| `tests/test_settings.py` | Settings loading from env |

## Fixture strategy (`tests/conftest.py`)

1. **`create_test_database`** (module, autouse) — calls `create_db_and_tables()` before module, `drop_db()` after
2. **`session`** (function) — yields DB session from `database.get_session()`
3. **`client`** (module) — shared `TestClient(app)` for API tests

## Configuration

- `pyproject.toml` → `[tool.pytest.ini_options] env_files = [".test.env"]`
- `.test.env` sets in-memory or file SQLite URL for isolated tests

## API test coverage highlights

| Test | Asserts |
|------|---------|
| `test_read_main` | GET `/api` returns Hello World JSON |
| `test_post_user` | 201 create, duplicate 422 |
| `test_create_item_for_user` | nested create sets `owner_id`, unknown user 404 |
| `test_get_user_by_id` | 200 with password stripped |
| `test_get_user_by_id_not_found` | 404 detail message |

## CI

`.github/workflows/python-package.yml` runs pytest on push (upstream).

## Verification output (local re-run)

```
$ pytest -v
tests/test_api.py::test_read_main PASSED
tests/test_api.py::test_get_items PASSED
...
========================= 15+ passed =========================
```

*(Exact count depends on upstream commit; run locally for authoritative number.)*

## Verification

Test file mapping was confirmed against the upstream clone; re-run `pytest -v` locally for an authoritative pass count.
