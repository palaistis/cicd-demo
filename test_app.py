import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello" in r.data

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200