from app.domain.interfaces.products_repository_interface import IProductsRepository
from app.domain.entities.products import Product
from app.shared.exceptions import EmptyProductListException

class ProductsService:
    def __init__(self, repository: IProductsRepository):
        self.repository = repository

    def get_products(self) -> list[Product]:
        products = self.repository.get_products()
        if not products:
            raise EmptyProductListException()
        return products
    