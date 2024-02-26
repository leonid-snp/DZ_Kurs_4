import pytest

from src.product import Product


def test_init_category(test_category):
    assert test_category.name == "Смартфоны"
    assert test_category.description == ("Смартфоны, как средство не только коммуникации,"
                                         " но и получение дополнительных функций для удобства жизни")


def test_add_product_in_category(test_category):
    test_category.add_product(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }))


def test_product_category(test_category):
    assert test_category.product == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                     'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                     'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']


def test_str_category(test_category):
    assert test_category.__str__() == "Смартфоны, количество продуктов: 3 шт."


def test_len_category(test_category):
    assert test_category.__len__() == 3


def test_add_product_in_category_raise(test_category):
    with pytest.raises(TypeError):
        test_category.add_product(test_category)
