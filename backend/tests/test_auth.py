# backend/tests/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    """
    Test the registration and login process.
    """
    # Test user registration
    register_response = client.post("/api/auth/register", json={"username": "testuser", "password": "testpass"})
    assert register_response.status_code == 200
    token = register_response.json().get("access_token")
    assert token is not None

    # Test user login
    login_response = client.post("/api/auth/login", json={"username": "testuser", "password": "testpass"})
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")
    assert token is not None
