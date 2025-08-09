import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_success():
    resposne = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "strongpassword",
        "role": "USER",
        "oauth_provider": "local"
    })
    assert resposne.status_code == 200
    data = resposne.json()
    assert "msg" in data
    assert data["msg"] == "User created successfully"
    assert "user_id" in data

def test_login_success():
    response = client.post(
        "/auth/login",
        data={"username": "test@example.com", "password": "strongpassword"}
    )

    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "brearer"

def test_login_fail_wrong_password():
    response = client.post(
        "/auth/login",
        data={"username": "test@example.com", "password": "wrongpassword"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid credentials"
