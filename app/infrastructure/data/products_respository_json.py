import json
from pathlib import Path
from typing import List
from app.domain.entities.products import Product, Price, Attribute

from app.domain.interfaces.products_repository_interface import IProductsRepository


class ProductsRepositoryJson(IProductsRepository):
    def __init__(self, data_file: str):
        self.data_file = Path(data_file)

    def _load_data(self) -> List[dict]:
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_products(self) -> List[Product]:
        data = self._load_data()
        return [self._map_to_entity(p) for p in data]

    def get_by_id(self, product_id: str) -> Product | None:
        data = self._load_data()
        for p in data:
            if p["id"] == product_id:
                return self._map_to_entity(p)
        return None

    @staticmethod
    def _map_to_entity(p: dict) -> Product:
        return Product(
            id=p["id"],
            title=p["title"],
            description=p.get("description", ""),
            price=Price(
                amount=p["price"]["amount"],
                currency=p["price"]["currency"]
            ),
            thumbnail=p["thumbnail"],
            category=p["category"],
            attributes=[
                Attribute(
                    name=a["name"],
                    value=a["value"]
                ) for a in p.get("attributes", [])
            ],
            images=p.get("images", []),
            stock=p.get("stock", 0),
            seller_id=p.get("seller_id", "")
        )
