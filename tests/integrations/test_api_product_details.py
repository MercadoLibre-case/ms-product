from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_product_details_sucesso():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_product_nao_encontrado():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"].startswith("Produto com ID")
