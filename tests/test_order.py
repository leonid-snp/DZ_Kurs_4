def test_init_order(test_order):
    assert test_order.count_product_pay == 5
    assert test_order.price == 180_000.0


def test_str_order(test_order):
    assert test_order.__str__() == "(Samsung Galaxy, 5, 180000.0)"


def test_len_order(test_order):
    assert test_order.__len__() == 5


def test_product_order(test_order):
    assert test_order.product == "Samsung Galaxy"
