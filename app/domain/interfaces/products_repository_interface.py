from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.products import Product


class IProductsRepository(ABC):
    @abstractmethod
    def get_products(self) -> List[Product] | None:
        pass
