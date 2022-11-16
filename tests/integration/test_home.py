from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_first_status_code_200():
    response = client.get("/first")
    assert response.status_code == 200


def test_first_json_response():
    response = client.get("/first")
    assert response.json() == {"msg": "Hello World"}
