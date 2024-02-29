from exceptions.exceptions import ProductQuantityZeroError
from src.category import Category
from src.order import Order
from src.product import Product


def main():
    cat = Category("Смартфоны", "Лучший дизайн", [
        Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 1),
    ])
    cat.add_product(Product('Iphone 15', '512GB, Gray space', 210000.0, 1))

    Order.create_order({
        "name": "Samsung Galaxy",
        "quantity": 1,
        "price": 180_000.0
    })


if __name__ == "__main__":
    try:
        main()
    except ProductQuantityZeroError as e:
        print(e)
    else:
        print("Товар был успешно добавлен")
    finally:
        print("Обработка добавления товара завершена")
