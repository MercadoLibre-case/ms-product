class Price:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency


class Attribute:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class Product:
    def __init__(
            self,
            id: str,
            title: str,
            price: Price,
            thumbnail: str,
            category: str,
            description: str = "",
            attributes: list[Attribute] = [],
            images: list[str] = [],
            stock: int = 0,
            seller_id: str = ""
    ):
        self.id = id
        self.title = title
        self.price = price
        self.thumbnail = thumbnail
        self.category = category
        self.description = description
        self.attributes = attributes
        self.images = images
        self.stock = stock
        self.seller_id = seller_id
