import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_usd_to_inr():
    r = client.post("/convert", json={"amount": 10, "source": "USD", "target": "INR"})
    assert r.status_code == 200
    body = r.json()
    assert body["result"] == 845.0


def test_same_currency_rate_one():
    r = client.post("/convert", json={"amount": 50, "source": "EUR", "target": "EUR"})
    assert r.json()["rate"] == 1.0


def test_invalid_currency():
    r = client.post("/convert", json={"amount": 1, "source": "USD", "target": "XYZ"})
    assert r.status_code == 400


def test_health_lists_currencies():
    r = client.get("/health")
    assert "USD" in r.json()["currencies"]
