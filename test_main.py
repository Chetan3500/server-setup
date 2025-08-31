from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my DevOps API!"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "healthy"


def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"server": "AWS EC2", "app": "FastAPI", "version": "1.0"}


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text
    assert "custom_requests_total" in response.text
