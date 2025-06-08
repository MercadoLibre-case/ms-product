from app.domain.interfaces.product_details_repository_interface import IProductDetailsRepository
from app.domain.entities.product_details import ProductDetails
from app.shared.exceptions import ProductNotFoundException


class ProductService:
    def __init__(self, repository: IProductDetailsRepository):
        self.repository = repository

    def get_product(self, product_id: str) -> ProductDetails:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ProductNotFoundException(product_id)
        return product
