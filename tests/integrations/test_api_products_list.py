from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_products_list():
    response = client.get("/products/")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0
    assert "id" in json_data[0]
    assert "title" in json_data[0]
