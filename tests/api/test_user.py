from asyncio import run

from fastapi.testclient import TestClient

from database.init_db import create_database


def test_create_user_status_code_201(client: TestClient):
    response = client.post("/user/create/", json={"name": "teste"})
    assert response.status_code == 201


def test_create_user_has_two_users(client: TestClient):
    run(create_database())
    response = client.get("/user/list")
    assert response.json() == 200
