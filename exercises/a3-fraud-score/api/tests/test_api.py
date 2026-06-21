import pytest
from fastapi.testclient import TestClient

from main import app, reset

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean():
    reset()
    yield


def test_create_and_score():
    r = client.post("/events", json={"account_id": "u1", "value": 1200, "channel": "web"})
    eid = r.json()["event_id"]
    s = client.patch(
        f"/events/{eid}/score",
        json={"event_id": eid, "score": 0.2, "band": "low", "flags": []},
    )
    assert s.json()["state"] == "scored"
