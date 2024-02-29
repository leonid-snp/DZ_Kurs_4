from exceptions.exceptions import ProductQuantityZeroError
from src.abstractlog import AbstractLog


class Order(AbstractLog):
    """
    Класс Заказы, покупает товар

    product (str) купленный продукт
    count_product_pay (int) количество купленного продукта
    price (float) итоговая стоимость продукта
    """
    def __init__(self, product: str, count_product_pay: int, price: float):
        self.__product = product
        self.count_product_pay = count_product_pay
        self.price = price

    def __str__(self) -> str:
        """
        Функция возвращает строковое отображения свойств класса

        :return (str) продукт, количество, стоимость
        """
        return f"({self.__product}, {self.count_product_pay}, {self.price})"

    def __len__(self) -> int:
        """
        Функция считает количество купленного товара

        :return (int) количество товара
        """
        return self.count_product_pay

    @property
    def product(self) -> str:
        """
        Функция геттер, возвращает приватный атрибут класса

        :return (str) продукт
        """
        return self.__product

    @classmethod
    def create_order(cls, product: dict) -> object:
        """
        Класс метод который создает новый объект Заказа из словаря

        :return (object) новый объект класса Заказы
        """
        if not product["quantity"] > 0:
            raise ProductQuantityZeroError()

        return cls(product["name"], product["quantity"], product["price"])
