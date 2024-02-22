import pytest
from src.category import Category
from src.product import Product
from utils.pars_json import creates_instance_class


@pytest.fixture
def test_category():
    return Category("Смартфоны", "Средство связи", ["a", "b", "c"])


@pytest.fixture
def test_product():
    return Product("Samsung", "Топ смартфон", 80_000.0, 7)


@pytest.fixture
def test_pars_json():
    return creates_instance_class()
