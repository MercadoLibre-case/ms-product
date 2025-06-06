from pydantic import BaseModel
from typing import List


class PriceSchema(BaseModel):
    amount: float
    currency: str


class ProductSchema(BaseModel):
    id: str
    title: str
    description: str
    price: PriceSchema
    images: List[str]
    stock: int
    seller_id: str
