# B2 — API Endpoint Map

**Target:** `ptrstn/fastapi-sqlalchemy-pytest-example` @ `19047d7`

All routes mount under `/api` via `api_router` in `src/mypackage/api/v1/router.py`.

## Endpoint table

| Method | Path | Handler | Request body | Response | Status codes |
|--------|------|---------|--------------|----------|--------------|
| GET | `/api/` | `get_home` | — | `{"Hello":"World"}` | 200 |
| GET | `/api/users/` | `read_users` | Query: `skip`, `limit` | `list[User]` | 200 |
| GET | `/api/users/{user_id}` | `read_user` | — | `User` | 200, 404 |
| POST | `/api/users/` | `create_user` | `UserCreate` | `User` | 201, 422 |
| GET | `/api/items/` | `read_items` | Query: `skip`, `limit` | `list[Item]` | 200 |
| POST | `/api/items/` | `create_item` | `ItemCreate` | `ItemCreate`* | 201 |
| POST | `/api/users/{user_id}/items/` | `create_item_for_user` | `ItemCreate` | `Item` | 201, 404 |

\* POST `/api/items/` returns `ItemCreate` schema (title/description only) — not full `Item` with id.

## Schema summary

| Model | Fields |
|-------|--------|
| `UserCreate` | `email`, `password` |
| `User` (response) | `id`, `email`, `is_active` — password excluded |
| `ItemCreate` | `title`, `description?` |
| `Item` (response) | `id`, `title`, `description?`, `owner_id` |

## Dependency injection

Every DB-touching route uses:

```python
db: Session = Depends(database.get_session)
```

Session is a generator yielding a SQLModel `Session` scoped per request.

## Error behavior

| Case | Code | Detail shape |
|------|------|--------------|
| Duplicate email on POST user | 422 | `"Email '{email}' already registered"` |
| Unknown user on nested item create | 404 | `"User with id '{id}' not found"` |
| Unknown user on GET by id | 404 | `"User with id '{id}' not found"` |

## OpenAPI

Auto-generated at `/docs` and `/openapi.json` when running uvicorn.
