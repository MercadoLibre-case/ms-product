class ApplicationException(Exception):
    """Exceção base para erros da aplicação."""
    pass


class ProductNotFoundException(ApplicationException):
    """Exceção lançada quando um produto não é encontrado."""

    def __init__(self, product_id: str):
        super().__init__(f"Produto com ID '{product_id}' não encontrado.")
        self.product_id = product_id


class EmptyProductListException(ApplicationException):
    """Exceção lançada quando a lista de produtos vier Nula"""

    def __init__(self):
        super().__init__("Lista de produtos está vazia.")
