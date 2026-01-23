"""
Integration tests for the SimLab API endpoints
"""

from starlette.testclient import TestClient
from simlab.main import app

client = TestClient(app)

def test_create_run():
    """
    Test POST /runs endpoint returns 201
    """
    payload = {
        "sim_type": "test",
        "params": {"value": 123}
    }

    response = client.post("/runs", json=payload)
    assert response.status_code == 201

def test_create_run_validation_error():
    """
    Test POST /runs endpoint returns 422 from bad payload
    """
    bad_payload = {
        "params": {"value": 123}
    }

    response = client.post("/runs", json=bad_payload)
    assert response.status_code == 422

def test_list_runs():
    """
    Test GET /runs returns two records after 2 post creation calls
    """
    client.post("/runs", json={"sim_type": "a", "params": {"x": 1}})
    client.post("/runs", json={"sim_type": "b", "params": {"y": 2}})

    response = client.get("/runs")
    assert response.status_code == 200

    data = response.json()
    assert len(data) >= 2

def test_get_run():
    """
    Test GET /runs/{id} request
    """
    payload = {
        "sim_type": "test",
        "params": {"value": 123}
    }

    client.post("/runs", json=payload)

    response = client.get("/runs/1")
    assert response.status_code == 200

def test_list_runs_with_filters():
    """
    Test GET /runs with query parameters: status and sim_type
    """
    # Create multiple runs
    client.post("/runs", json={"sim_type": "chemistry", "params": {"samples": 10}})
    client.post("/runs", json={"sim_type": "physics", "params": {"samples": 5}})
    client.post("/runs", json={"sim_type": "chemistry", "params": {"samples": 20}})

    # Filter by sim_type
    response = client.get("/runs", params={"sim_type": "chemistry"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2

    # Filter by status (assuming default "pending")
    response = client.get("/runs", params={"status": "pending"})
    assert response.status_code == 200

    # Filter by both sim_type and status
    response = client.get("/runs", params={"sim_type": "physics", "status": "pending"})
    assert response.status_code == 200
