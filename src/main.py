from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from utils.pars_json import creates_instance_class


def main():
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180_000.0, 0)
    Smartphone("Samsung Galaxy", "Хорошая камера", 180_000.0, 5, 2.5, "C23 Ultra", 6, "Серый цвет")
    LawnGrass("Газон", "Густая красивая трава", 150.0, 200, "Китай", 3.5, "Зеленый цвет")


if __name__ == "__main__":
    main()
