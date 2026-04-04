from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app, )


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "hello k8s!"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ready():
    with TestClient(app) as client:
        response = client.get("/ready")
        assert response.status_code == 200
        assert response.json()["status"] == "ready"

