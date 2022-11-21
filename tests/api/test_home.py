from fastapi.testclient import TestClient


def test_first_status_code_200(client: TestClient):
    response = client.get("/first")
    assert response.status_code == 200


def test_first_json_response(client: TestClient):
    response = client.get("/first")
    assert response.json() == {"msg": "Hello World"}
