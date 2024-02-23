class Category:
    """
    name: (str) название категории
    description: (str) описание категории
    product: (list) список продуктов
    count_category: (int) количество категорий (default 0)
    count_product: (int) количество продуктов (default 0)
    """
    name: str
    description: str
    product: list
    count_category: int = 0
    count_product: int = 0

    def __init__(self, name: str, description: str, product: list) -> None:
        self.name = name
        self.description = description
        self.product = product
        self.count_category += 1
        self.count_product += len(product)
