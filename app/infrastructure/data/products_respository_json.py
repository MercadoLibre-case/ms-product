import json
from pathlib import Path
from typing import List

from app.domain.entities.products import Product, Price
from app.domain.interfaces.products_repository_interface import IProductsRepository


class ProductsRepositoryJson(IProductsRepository):
    def __init__(self, data_file: str):
        self.data_file = Path(data_file)

    def _load_data(self) -> list[dict]:
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_products(self) -> List[Product] | None:
        data = self._load_data()
        if not data:
            return None

        return [
            Product(
                id=p["id"],
                title=p["title"],
                price=Price(
                    amount=p["price"]["amount"],
                    currency=p["price"]["currency"]
                ),
                thumbnail=p["thumbnail"],
                category=p["category"]
            )
            for p in data
        ]
