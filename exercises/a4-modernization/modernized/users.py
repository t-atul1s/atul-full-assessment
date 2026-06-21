"""Modernized user helpers (type hints, dataclasses, comprehensions)."""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class User:
    email: str
    name: str
    active: bool = True


def load_users(records: Iterable[dict]) -> list[User]:
    return [
        User(email=r["email"], name=r["name"], active=r.get("active", True))
        for r in records
        if "email" in r and "name" in r
    ]


def find_by_email(users: Iterable[User], email: str) -> User | None:
    return next((u for u in users if u.email == email), None)
