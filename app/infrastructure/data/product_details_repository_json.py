import json
from pathlib import Path

from app.domain.entities.product_details import ProductDetails, Attributes, Price
from app.domain.interfaces.product_details_repository_interface import IProductDetailsRepository


class ProductDetailsRepositoryJson(IProductDetailsRepository):
    def __init__(self, data_file: str):
        self.data_file = Path(data_file)

    def _load_data(self) -> list[dict]:
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_by_id(self, product_id: str) -> ProductDetails | None:
        products = self._load_data()
        for p in products:
            if p["id"] == product_id:
                return ProductDetails(
                    id=p["id"],
                    title=p["title"],
                    description=p["description"],
                    attributes=[
                        Attributes(
                            name=attribuites["name"],
                            value=attribuites["value"]
                        )
                        for attribuites in p["attributes"]
                    ],
                    price=Price(
                        amount=p["price"]["amount"],
                        currency=p["price"]["currency"],
                    ),
                    images=p["images"],
                    stock=p["stock"],
                    seller_id=p["seller_id"],
                )
        return None
