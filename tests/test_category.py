def test_init_category(test_category):
    assert test_category.name == "Смартфоны"
    assert test_category.description == "Средство связи"
    assert test_category.product == ["a", "b", "c"]
    assert test_category.count_product == 3
    assert test_category.count_category == 1
