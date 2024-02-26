def test_iter_and_next_product_iterator(test_iterator):
    list_product = [i for i in test_iterator]
    assert list_product == ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                            'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                            'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']
