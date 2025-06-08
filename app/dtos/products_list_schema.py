from pydantic import BaseModel


class PriceSchema(BaseModel):
    amount: float
    currency: str


class ProductListSchema(BaseModel):
    id: str
    title: str
    price: PriceSchema
    thumbnail: str
    category: str
