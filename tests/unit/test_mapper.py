from app.domain.entities.product import Product, Price
from app.dtos.mapper import product_to_schema


def test_product_to_schema():
    product = Product(
        id="123",
        title="Teste",
        description="Desc",
        price=Price(10.0, "USD"),
        images=["img.jpg"],
        stock=3,
        seller_id="s1"
    )

    dto = product_to_schema(product)

    assert dto.id == "123"
    assert dto.price.amount == 10.0
