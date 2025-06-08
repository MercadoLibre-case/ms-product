class Price:
    def __init__(self,
                 amount: float,
                 currency: str):
        self.amount = amount
        self.currency = currency

class Product:
    def __init__(
        self,
        id: str,
        title: str,
        price: Price,
        thumbnail: str,
        category: str,
    ):
        self.id = id
        self.title = title
        self.price = price
        self.thumbnail = thumbnail
        self.category = category
