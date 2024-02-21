class Category:
    name: str
    description: str
    product: list
    count_category: int = 0
    count_product: int = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        self.count_category += 1git
        self.count_product += len(product)
