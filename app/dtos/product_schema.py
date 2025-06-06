from pydantic import BaseModel
from typing import List

class AttributesSchema(BaseModel):
    name: str
    value: str


class PriceSchema(BaseModel):
    amount: float
    currency: str


class ProductSchema(BaseModel):
    id: str
    title: str
    description: str
    price: PriceSchema
    attributes: List[AttributesSchema]
    images: List[str]
    stock: int
    seller_id: str
