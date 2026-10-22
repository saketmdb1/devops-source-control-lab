import os
import requests


BASE_URL = os.environ["UAT_BASE_URL"].rstrip("/")


def test_uat_home_endpoint():
    response = requests.get(f"{BASE_URL}/", timeout=15)

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Hello from Azure Container Apps! Deployment Added"
    )


def test_uat_health_endpoint():
    response = requests.get(f"{BASE_URL}/health", timeout=15)

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
