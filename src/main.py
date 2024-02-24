from src.category import Category
from src.product import Product
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    print("Выводим список категорий на экран:")
    cat = Category(*instance_category[0])
    print(cat.name, cat.description, cat.product, sep="\n")
    print("Добавим еще один товар")
    cat.add_product(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }))
    print("Выводим список категорий на экран:")
    print(cat.name, cat.description, cat.product, sep="\n")


    # print("\nВыводим список продуктов на экран:")
    # for product in instance_product:
    #     pro = Product(*product)
    #     print(pro.name, pro.description, pro.price, pro.quantity, sep="\n")


if __name__ == "__main__":
    main()
