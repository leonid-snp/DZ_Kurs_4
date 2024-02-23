from src.category import Category
from src.product import Product
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    print("Выводим список категорий на экран:")
    for category in instance_category:
        cat = Category(*category)
        print(cat.name, cat.description, cat.product, sep=" | ")

    print("\nВыводим список продуктов на экран:")
    for product in instance_product:
        pro = Product(*product)
        print(pro.name, pro.description, pro.price, pro.quantity, sep=" | ")


if __name__ == "__main__":
    main()
