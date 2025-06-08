import pytest
from app.domain.services.products_service import ProductsService
from app.domain.entities.products import Product, Price, Attribute
from app.domain.interfaces.products_repository_interface import IProductsRepository
from app.shared.exceptions import ProductNotFoundException


class FakeRepo(IProductsRepository):
    def __init__(self):
        self.products = [
            Product(
                id="1",
                title="Produto Teste",
                description="Descrição",
                price=Price(10.0, "USD"),
                thumbnail="img.jpg",
                category="categoria",
                attributes=[
                    Attribute(name="Tela", value="6.5'")
                ],
                images=["img1", "img2"],
                stock=10,
                seller_id="seller1"
            )
        ]

    def get_products(self):
        return self.products

    def get_by_id(self, product_id: str):
        for p in self.products:
            if p.id == product_id:
                return p
        return None


def test_deve_retornar_produto_por_id():
    service = ProductsService(FakeRepo())
    product = service.get_product("1")
    assert product.id == "1"
    assert product.title == "Produto Teste"


def test_deve_lancar_excecao_para_produto_nao_encontrado():
    service = ProductsService(FakeRepo())
    with pytest.raises(ProductNotFoundException):
        service.get_product("999")
