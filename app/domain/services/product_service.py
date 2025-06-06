from app.domain.interfaces.product_repository_interface import IProductRepository
from app.domain.entities.product import Product
from app.shared.exceptions import ProductNotFoundException


class ProductService:
    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def get_product(self, product_id: str) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ProductNotFoundException(product_id)
        return product
