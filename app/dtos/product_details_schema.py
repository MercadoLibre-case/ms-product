from pydantic import BaseModel
from typing import List

class AttributesSchema(BaseModel):
    name: str
    value: str


class PriceDetailsSchema(BaseModel):
    amount: float
    currency: str


class ProductDetailsSchema(BaseModel):
    id: str
    title: str
    description: str
    price: PriceDetailsSchema
    attributes: List[AttributesSchema]
    images: List[str]
    stock: int
    seller_id: str
