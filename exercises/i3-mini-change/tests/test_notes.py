import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_pagination_default():
    r = client.get("/notes")
    assert r.status_code == 200
    assert len(r.json()) == 10
    assert r.json()[0]["id"] == 1


def test_pagination_skip():
    r = client.get("/notes?skip=10&limit=5")
    body = r.json()
    assert len(body) == 5
    assert body[0]["id"] == 11
