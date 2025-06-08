from app.domain.entities.product_details import ProductDetails, Price, Attributes
from app.dtos.mapper import product_details_to_schema


def test_product_details_to_schema():
    product = ProductDetails(
        id="123",
        title="Teste",
        description="Desc",
        attributes=[
            Attributes(
                name="NFC",
                value="Sim"
            )
        ],
        price=Price(10.0, "USD"),
        images=["img.jpg"],
        stock=3,
        seller_id="s1"
    )

    dto = product_details_to_schema(product)

    assert dto.id == "123"
    assert dto.price.amount == 10.0
