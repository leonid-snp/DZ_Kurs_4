import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def test_category():
    return Category("Смартфоны", "Средство связи", ["a", "b", "c"])


@pytest.fixture
def test_product():
    return Product("Samsung", "Топ смартфон", 80_000.0, 7)
