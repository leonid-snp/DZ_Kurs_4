def test_init_product(test_product):
    assert test_product.name == "Samsung Galaxy C23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180_000.0
    assert test_product.quantity == 5
