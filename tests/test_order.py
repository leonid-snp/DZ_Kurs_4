import pytest

from exceptions.exceptions import ProductQuantityZeroError
from src.order import Order


def test_init_order(test_order):
    assert test_order.count_product_pay == 5
    assert test_order.price == 180_000.0


def test_str_order(test_order):
    assert test_order.__str__() == "(Samsung Galaxy, 5, 180000.0)"


def test_len_order(test_order):
    assert test_order.__len__() == 5


def test_product_order(test_order):
    assert test_order.product == "Samsung Galaxy"


def test_create_raise_order():
    with pytest.raises(ProductQuantityZeroError):
        assert Order.create_order({
            "name": "Samsung Galaxy",
            "quantity": 0,
            "price": 180_000.0
        })


def test_create_order():
    assert Order.create_order({
        "name": "Samsung Galaxy",
        "quantity": 1,
        "price": 180_000.0
    })
