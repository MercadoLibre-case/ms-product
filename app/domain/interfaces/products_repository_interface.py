from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.products import Product


class IProductsRepository(ABC):
    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Product | None:
        pass

    @abstractmethod
    def get_related_products(self, product_id: str) -> List[Product]:
        pass
