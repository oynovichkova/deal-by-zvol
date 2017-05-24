delete = [
    {
        'name': 'Архивирование существующей сделки',
        'description': '',
        'precondition': {
            "create_deal": True,
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        },
    },
    {
        'name': 'Архивирование существующей сделкис проверкой выставляемого флага в базе',
        'description': '',
        'precondition': {
            "create_deal": True,
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'sql': {
                'request': 'SELECT archived FROM deal WHERE id=%s',
                'result': [(True,)]
            }
        }
    },
    {
        'name': 'Повторное архивирование существующей сделки',
        'description': '',
        'precondition': {
            "create_deal": True,
            "delete_deal": True,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        },
    },
    {
        'name': 'Архивирование несуществующей сделки',
        'description': '',
        'precondition': {
            "create_deal": False,
            "delete_deal": False,
            'data': {
                'dealId': 123123123123123,
            },
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        },
    },
    {
        'name': 'Удаление нескольких сделок',
        'description': '',
        'precondition': {
            "create_deal": False,
            "delete_deal": False,
            'data': {
                'dealId': '45,46',
            },
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        },
    },
]

pagination = {
    'negative': [
        {
            'name': 'Невалидное значение номера страницы строкового типа',
            'description': '',
            'data': {
                'page': 'a',
                'size': 20,
            },
            'expected': {
                "success": True,
                "page": {
                    "size": 20,
                    "number": 0
                }
            }
        },
        {
            'name': 'Невалидное значение размера страницы строкового типа',
            'description': '',
            'data': {
                'page': 1,
                'size': 'b',
            },
            'expected': {
                "success": True,
                "page": {
                    "size": 10,
                    "number": 1
                }
            }
        },
        {
            'name': 'Невалидное значение номера страницы вещественного типа',
            'description': '',
            'data': {
                'page': 1.5,
                'size': 20,
            },
            'expected': {
                "success": True,
                "page": {
                    "size": 20,
                    "number": 0
                }
            }
        },
        {
            'name': 'Невалидное значение размера страницы вещественного типа',
            'description': '',
            'data': {
                'page': 1,
                'size': 10.5,
            },
            'expected': {
                "success": True,
                "page": {
                    "size": 10,
                    "number": 1
                }
            }
        },
    ],
    'signature': [
        {
            'name': 'Проверка сигнатуры метаинформации пагинации',
            'description': '',
            'data': {
                'page': 1,
                'size': 20,
            },
            'expected': {
                "success": True,
                "page": {
                    "size": 10,
                    "totalElements": 5344,
                    "totalPages": 535,
                    "number": 0
                },
            }
        },
    ]
}