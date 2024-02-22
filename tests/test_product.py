def test_init_product(test_product):
    assert test_product.name == "Samsung"
    assert test_product.description == "Топ смартфон"
    assert test_product.price == 80_000.0
    assert test_product.quantity == 7
