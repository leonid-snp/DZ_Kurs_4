def test_json(test_pars_json):
    assert test_pars_json[0] == [('Смартфоны',
                                  'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                                  [{'name': 'Samsung Galaxy C23 Ultra',
                                    'description': '256GB, Серый цвет, 200MP камера',
                                    'price': 180000.0,
                                    'quantity': 5
                                    },
                                   {'name': 'Iphone 15',
                                    'description': '512GB, Gray space',
                                    'price': 210000.0,
                                    'quantity': 8
                                    },
                                   {'name': 'Xiaomi Redmi Note 11',
                                    'description': '1024GB, Синий',
                                    'price': 31000.0,
                                    'quantity': 14
                                    }]),
                                 ('Телевизоры',
                                  'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                                  [{'name': '55" QLED 4K',
                                    'description': 'Фоновая подсветка',
                                    'price': 123000.0,
                                    'quantity': 7
                                    }])]

    assert test_pars_json[1] == [('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
                                 ('Iphone 15', '512GB, Gray space', 210000.0, 8),
                                 ('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14),
                                 ('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)]
