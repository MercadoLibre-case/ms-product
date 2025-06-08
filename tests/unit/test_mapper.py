from app.domain.entities.products import Product, Price, Attribute
from app.dtos.mapper import product_to_details_schema


def test_product_details_to_schema():
    product = Product(
        id="123",
        title="Produto Teste",
        description="Descrição completa",
        price=Price(99.99, "USD"),
        thumbnail="thumb.jpg",
        category="categoria1",
        attributes=[
            Attribute(name="Memória", value="128GB")
        ],
        images=["img1.jpg", "img2.jpg"],
        stock=10,
        seller_id="vendedor1"
    )

    schema = product_to_details_schema(product)

    assert schema.id == "123"
    assert schema.price.amount == 99.99
    assert schema.attributes[0].name == "Memória"
