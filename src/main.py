from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    cat = Smartphone(*instance_category[0])
    print(cat.name)


if __name__ == "__main__":
    main()
