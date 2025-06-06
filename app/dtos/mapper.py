from app.domain.entities.product import Product
from app.dtos.product_schema import ProductSchema, PriceSchema, AttributesSchema


def product_to_schema(product: Product) -> ProductSchema:
    return ProductSchema(
        id=product.id,
        title=product.title,
        description=product.description,
        attributes=[
            AttributesSchema(
                name=attribute.name,
                value=attribute.value
            )
            for attribute in product.attributes
        ],
        price=PriceSchema(
            amount=product.price.amount,
            currency=product.price.currency,
        ),
        images=product.images,
        stock=product.stock,
        seller_id=product.seller_id,
    )
