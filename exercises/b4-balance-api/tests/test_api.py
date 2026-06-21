import pytest
from fastapi.testclient import TestClient

from main import app, reset

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean():
    reset()
    yield
    reset()


def test_credit_and_balance():
    r = client.post("/transactions", json={"kind": "credit", "amount": 250})
    assert r.status_code == 201
    assert client.get("/balance").json()["balance"] == 250


def test_debit_reduces_balance():
    client.post("/transactions", json={"kind": "credit", "amount": 100})
    r = client.post("/transactions", json={"kind": "debit", "amount": 30})
    assert r.status_code == 201
    assert client.get("/balance").json()["balance"] == 70


def test_debit_over_balance_400():
    client.post("/transactions", json={"kind": "credit", "amount": 10})
    r = client.post("/transactions", json={"kind": "debit", "amount": 50})
    assert r.status_code == 400


def test_invalid_amount_422():
    assert client.post("/transactions", json={"kind": "credit", "amount": 0}).status_code == 422


def test_list_newest_first():
    client.post("/transactions", json={"kind": "credit", "amount": 1})
    client.post("/transactions", json={"kind": "credit", "amount": 2})
    amounts = [t["amount"] for t in client.get("/transactions").json()]
    assert amounts == [2, 1]
