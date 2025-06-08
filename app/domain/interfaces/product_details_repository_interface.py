from abc import ABC, abstractmethod
from app.domain.entities.product_details import ProductDetails


class IProductDetailsRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: str) -> ProductDetails | None:
        pass
