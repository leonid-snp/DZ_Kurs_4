import pytest
from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from utils.pars_json import creates_instance_class


@pytest.fixture
def test_category():
    instance_category, instance_product = creates_instance_class()
    for category in instance_category:
        return Category(*category)


@pytest.fixture
def test_product():
    instance_category, instance_product = creates_instance_class()
    for product in instance_product:
        return Product(*product)


@pytest.fixture
def test_pars_json():
    return creates_instance_class()


@pytest.fixture
def test_iterator():
    instance_category, instance_product = creates_instance_class()
    return ProductIterator(instance_category[0][2])


@pytest.fixture
def test_smartphone():
    return Smartphone("Samsung Galaxy", "Хорошая камера", 180_000.0, 5, 2.5, "C23 Ultra", 6, "Серый цвет")


@pytest.fixture
def test_lawn_grass():
    return LawnGrass("Газон", "Густая красивая трава", 150.0, 200, "Китай", 3.5, "Зеленый цвет")
