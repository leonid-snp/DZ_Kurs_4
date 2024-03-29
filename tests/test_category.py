import pytest

from exceptions.exceptions import ProductQuantityZeroError
from src.category import Category
from src.product import Product


def test_init_category(test_category):
    assert test_category.name == "Смартфоны"
    assert test_category.description == ("Смартфоны, как средство не только коммуникации,"
                                         " но и получение дополнительных функций для удобства жизни")


def test_add_product_in_category(test_category, test_create_product):
    test_category.add_product(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }, test_create_product))


def test_product_category(test_category):
    assert test_category.product == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                     'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                     'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']


def test_copy_product_category(test_category):
    assert test_category.copy_product[0].name == "Samsung Galaxy C23 Ultra"


def test_str_category(test_category):
    assert test_category.__str__() == "Смартфоны, количество продуктов: 3 шт."


def test_len_category(test_category):
    assert test_category.__len__() == 3


def test_add_product_in_category_type_error(test_category):
    with pytest.raises(TypeError):
        test_category.add_product(test_category)


def test_add_product_in_category_value_error(test_category, test_raise_product):
    with pytest.raises(ProductQuantityZeroError):
        test_category.add_product(test_raise_product)


def test_get_average_product_price_category(test_category):
    assert test_category.get_average_product_price() == 111_629.6


def test_get_average_product_price_zero_division_category(test_raise_category):
    assert test_raise_category.get_average_product_price() == 0.0
