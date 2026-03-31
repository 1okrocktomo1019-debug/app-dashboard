import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_index_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200


def test_index_contains_app_names(client):
    res = client.get("/")
    html = res.data.decode("utf-8")
    assert "X → Threads" in html
    assert "Gemini" in html


def test_index_contains_links(client):
    res = client.get("/")
    html = res.data.decode("utf-8")
    assert "railway.app" in html
