class Product:
    """
    name: (str) название продукта
    description: (str) описание продукта
    price: (float) цена товара
    quantity: (int) остаток товара
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def creates_product(cls, product: dict) -> object:
        """
        Классметод который принимает словарь и создает новый объект класса Product

        :return (object) объект класса Product
        """
        return cls(product["name"], product["description"], product["price"], product["quantity"])
