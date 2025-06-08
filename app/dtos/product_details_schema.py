from typing import List
from pydantic import BaseModel


class PriceSchema(BaseModel):
    amount: float
    currency: str


class AttributeSchema(BaseModel):
    name: str
    value: str


class ProductDetailsSchema(BaseModel):
    id: str
    title: str
    description: str
    price: PriceSchema
    thumbnail: str
    images: List[str]
    category: str
    attributes: List[AttributeSchema]
    stock: int
    seller_id: str
