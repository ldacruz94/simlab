from starlette.testclient import TestClient
from simlab.main import app

client = TestClient(app)

def test_create_run():
    payload = {
        "sim_type": "test",
        "params": {"value": 123}
    }

    response = client.post("/runs", json=payload)
    assert response.status_code == 201

def test_create_run_validation_error():
    bad_payload = {
        "params": {"value": 123}
    }

    response = client.post("/runs", json=bad_payload)
    assert response.status_code == 422

def test_list_runs():
    client.post("/runs", json={"sim_type": "a", "params": {"x": 1}})
    client.post("/runs", json={"sim_type": "b", "params": {"y": 2}})

    response = client.get("/runs")
    assert response.status_code == 200

    data = response.json()
    assert len(data) >= 2

def test_get_run():
    payload = {
        "sim_type": "test",
        "params": {"value": 123}
    }

    client.post("/runs", json=payload)

    response = client.get("/runs/1")
    assert response.status_code == 200