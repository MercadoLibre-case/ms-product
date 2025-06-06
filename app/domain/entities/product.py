from typing import List

class Attributes:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class Price:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency


class Product:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        attributes: List[Attributes],
        price: Price,
        images: List[str],
        stock: int,
        seller_id: str,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.attributes = attributes
        self.price = price
        self.images = images
        self.stock = stock
        self.seller_id = seller_id
