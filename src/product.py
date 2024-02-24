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
        self._price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Функция отображает определенные данные в строковом формате

        :return (str) название продукта, цена, остаток
        """
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """
        Геттер для свойства цены

        :return (float) цена продукта
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для свойства цены, устанавливает новое значение если оно больше 0
        """
        if value <= 0:
            print("цена введена некорректная")
        elif value < self._price:
            while True:
                answer = input("Вы уверены что хотите понизить цену: (y/n)").lower()
                if answer == "y":
                    self._price = value
                    break

                elif answer == "n":
                    self._price = self._price
                    break

        else:
            self._price = value

    @classmethod
    def creates_product(cls, product: dict, list_product: list) -> object:
        """
        Классметод который принимает словарь и создает новый объект класса Product

        :product (dict) продукт по которому создаст объект
        :list_product (list) список с уже имеющимися продуктами

        :return (object) объект класса Product
        """
        for name in list_product:
            if product["name"] not in name:
                return cls(product["name"], product["description"], product["price"], product["quantity"])
