from src.category import Category
from src.product import Product
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()

    # print("Выводим список категорий на экран:")
    # cat = Category(*instance_category[0])
    # print(cat.name, cat.description, cat.product, sep="\n")
    #
    # print("\nДобавим еще один товар")
    # cat.add_product(Product.creates_product({
    #     "name": "Samsung Galaxy C23 Ultra",
    #     "description": "Влагозащищенный корпус",
    #     "price": 190_000.0,
    #     "quantity": 5
    # }, cat.product))
    #
    # print("Выводим список категорий на экран:")
    # print(cat.name, cat.description, cat.product, sep="\n")


    print("Выводим список продуктов на экран")
    pro = Product(*instance_product[1])
    print(pro.name, pro.description, pro.price, pro.quantity, sep="\n")
    print("\nХотим поменять цену")
    pro.price = 200_000.0
    print(f"Новая цена {pro.price}")



if __name__ == "__main__":
    main()
