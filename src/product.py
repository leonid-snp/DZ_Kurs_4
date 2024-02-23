class Product:
    """
    name: (str) название продукта
    description: (str) описание продукта
    price: (float) цена товара
    quantity: (int) остаток товара
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
