from app.domain.entities.products import Product
from app.dtos.products_list_schema import ProductListSchema, PriceSchema as PriceListSchema
from app.dtos.product_details_schema import ProductDetailsSchema, AttributeSchema, PriceSchema as PriceDetailsSchema
from typing import List


def product_to_list_schema(product: Product) -> ProductListSchema:
    return ProductListSchema(
        id=product.id,
        title=product.title,
        price=PriceListSchema(
            amount=product.price.amount,
            currency=product.price.currency
        ),
        thumbnail=product.thumbnail,
        category=product.category
    )


def products_list_to_schema(products: List[Product]) -> List[ProductListSchema]:
    return [product_to_list_schema(p) for p in products]


def product_to_details_schema(product: Product) -> ProductDetailsSchema:
    return ProductDetailsSchema(
        id=product.id,
        title=product.title,
        description=product.description,
        price=PriceDetailsSchema(
            amount=product.price.amount,
            currency=product.price.currency
        ),
        thumbnail=product.thumbnail,
        images=product.images,
        category=product.category,
        attributes=[
            AttributeSchema(
                name=attr.name,
                value=attr.value
            ) for attr in product.attributes
        ],
        stock=product.stock,
        seller_id=product.seller_id
    )
