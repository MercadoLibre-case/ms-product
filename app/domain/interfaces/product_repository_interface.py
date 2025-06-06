from abc import ABC, abstractmethod
from app.domain.entities.product import Product


class IProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: str) -> Product | None:
        pass
