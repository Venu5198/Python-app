# tests/test_app.py
from my_app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_add():
    client = app.test_client()
    response = client.get("/add/2/3")
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 5
