import pytest
from app.domain.entities.product_details import ProductDetails, Price, Attributes
from app.domain.services.product_details_service import ProductService
from app.domain.interfaces.product_details_repository_interface import IProductDetailsRepository
from app.shared.exceptions import ProductNotFoundException


# Mock do repositório
class FakeRepo(IProductDetailsRepository):
    def __init__(self):
        self.products = {
            "1": ProductDetails(
                id="1",
                title="Produto Teste",
                description="Descrição",
                attributes=[
                    Attributes(
                        name="NFC",
                        value="Sim"
                    )
                ],
                price=Price(100, "USD"),
                images=["url1", "url2"],
                stock=5,
                seller_id="vendedor1"
            )
        }

    def get_by_id(self, product_id: str):
        return self.products.get(product_id)


def test_deve_retornar_produto_existente():
    service = ProductService(FakeRepo())
    product = service.get_product("1")
    assert product.id == "1"
    assert product.title == "Produto Teste"


def test_deve_lancar_excecao_para_produto_inexistente():
    service = ProductService(FakeRepo())
    with pytest.raises(ProductNotFoundException):
        service.get_product("999")
