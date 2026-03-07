import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_init_database(client):
    response = client.get("/init")
    assert response.status_code == 200


def test_add_member(client):
    response = client.get("/add")
    assert response.status_code == 200


def test_get_members(client):
    response = client.get("/members")
    assert response.status_code == 200