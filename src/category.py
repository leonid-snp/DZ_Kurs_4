from exceptions.exceptions import ProductQuantityZeroError
from src.abstractlog import AbstractLog
from src.product import Product


class Category(AbstractLog):
    """
    name: (str) название категории
    description: (str) описание категории
    product: (list) список продуктов
    count_category: (int) количество категорий (default 0)
    count_product: (int) количество продуктов (default 0)
    """
    count_category: int = 0
    count_product: int = 0

    def __init__(self, name: str, description: str, product: list) -> None:
        self.name = name
        self.description = description
        for elem in product:
            if elem.quantity == 0:
                raise ProductQuantityZeroError()
            else:
                self.__product = product
        self.count_category += 1
        self.count_product += len(product)

    def __str__(self) -> str:
        """
        Функция отображает определенные данные в строковом формате

        :return (str) название категории и количество продуктов
        """
        return f"{self.name}, количество продуктов: {len(self.__product)} шт."

    def __len__(self) -> int:
        """
        Функция считает количество продуктов

        :return (int) количество продуктов
        """
        return len(self.__product)

    def add_product(self, value: object) -> None:
        """
        Функция добавляет в список продуктов новый продукт
        """
        if not isinstance(value, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")

        if value.quantity == 0:
            raise ProductQuantityZeroError("ProductQuantityZeroError: "
                                           "Товар с нулевым количеством не может быть добавлен")

        self.__product.append(value)

    @property
    def product(self) -> list:
        """
        Функция геттер которая выводит на экран список товаров в специальном формате

        :return (list) список продуктов
        """
        list_products = []
        for product in self.__product:
            list_products.append(f"{Product.__str__(product)}")

        return list_products

    def get_average_product_price(self) -> float:
        """
        Функция считает средний ценник всех товаров

        :return (float) средняя цена товара
        """
        try:
            price = 0
            quantity = 0
            for product in self.__product:
                price += (product.price * product.quantity)
                quantity += product.quantity

            result = round((price / quantity), 1)
        except ProductQuantityZeroError:
            return 0.0
        else:
            return result
