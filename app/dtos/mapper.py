from typing import List

from app.domain.entities.product_details import ProductDetails
from app.domain.entities.products import Product
from app.dtos.product_details_schema import ProductDetailsSchema, PriceDetailsSchema, AttributesSchema
from app.dtos.products_schema import ProductSchema, PriceSchema


def product_details_to_schema(product_details: ProductDetails) -> ProductDetailsSchema:
    return ProductDetailsSchema(
        id=product_details.id,
        title=product_details.title,
        description=product_details.description,
        attributes=[
            AttributesSchema(
                name=attribute.name,
                value=attribute.value
            )
            for attribute in product_details.attributes
        ],
        price=PriceDetailsSchema(
            amount=product_details.price.amount,
            currency=product_details.price.currency,
        ),
        images=product_details.images,
        stock=product_details.stock,
        seller_id=product_details.seller_id,
    )


def products_to_schema(products: List[Product]) -> List[ProductSchema]:
    return [
        ProductSchema(
            id=product.id,
            title=product.title,
            price=PriceSchema(
                amount=product.price.amount,
                currency=product.price.currency,
            ),
            thumbnail=product.thumbnail,
            category=product.category
        )
        for product in products
    ]
