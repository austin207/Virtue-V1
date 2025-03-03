# backend/tests/test_chat.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint_unauthenticated():
    """
    Test that the chat endpoint returns 401 when not authenticated.
    """
    response = client.post("/api/chat/", json={"session_id": "test", "message": "Hello"})
    assert response.status_code == 401

# Additional tests for authenticated chat endpoints would require
# setting up proper authentication and mocking the LLM responses.
