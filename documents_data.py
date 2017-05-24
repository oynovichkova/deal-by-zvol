post = {
    "required": [
        {
            'name': 'Позитивный тест исключительно с корректными обязательными параметрами',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
            },
            'expected': {
                "success": True,
                "data": [
                    {
                        "userId": 1,
                        "documentTypeId": 20010,
                        "modifiedBy": 2,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и не существующим fileId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "fileId": 1000000000000,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 404,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и fileId, который уже был ранее привязан',
            'description': '',
            'precondition': {
                "post_doc_to_deal": {
                    "documentTypeId": 20010,
                    "userId": 1,
                },
            },
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 500,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с пустым fileId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "fileId": None,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "internalMessage": "may not be null",
                        "userMessage": None,
                        "argument": {
                            "field": "fileId",
                            "value": "null"
                        }
                    }
                ],
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с вещественным fileId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "fileId": -123.123,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 404,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с логическим fileId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "fileId": True,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с строковым fileId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "fileId": "string",
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и без userId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": None,
                "fileId": 123,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "internalMessage": "may not be null",
                        "userMessage": None,
                        "argument": {
                            "field": "userId",
                            "value": "null"
                        }
                    }
                ],
            }
        },
        # TODO: разобраться что значит userId и почему не проводится валидация на его существование
        # {
        #     'name': 'Негативный тест исключительно с обязательными параметрами c несуществующим userId',
        #     'description': '',
        #     'data': {
        #         "documentTypeId": 20010,
        #         "userId": 123123123123,
        #     },
        #     'expected': {
        #         "success": False,
        #         "errors": [
        #             {
        #                 "code": 404,
        #                 #"internalMessage": "ResourceNotFoundException: 404 Not Found",
        #                 "userMessage": None,
        #             }
        #         ]
        #     }
        # },
        # TODO: выяснить что это за поле, почему мы его не валидируем и почему на нём работает приведение типов
        # {
        #     'name': 'Негативный тест исключительно с обязательными параметрами и с вещественным userId',
        #     'description': '',
        #     'data': {
        #         "documentTypeId": 20010,
        #         "userId": -123.123,
        #     },
        #     'expected': {
        #         "success": False,
        #         "errors": [
        #             {
        #                 "code": 500,
        #                 "userMessage": None,
        #             }
        #         ]
        #     }
        # },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с логическим userId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": True,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с строковым userId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": "string",
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        # TODO: выяснить почему поле filename не помечено READONLY, хотя по факту данные из него в базу не сохраняются
        # TODO: выяснить почему поле filename не помечено READONLY, хотя по факту данные из него в базу не сохраняются
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с несуществующим documentTypeId',
            'description': '',
            'data': {
                "documentTypeId": 200100,
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 400,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с пустым documentTypeId',
            'description': '',
            'data': {
                "documentTypeId": None,
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с логическим documentTypeId',
            'description': '',
            'data': {
                "documentTypeId": True,
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с строковым documentTypeId',
            'description': '',
            'data': {
                "documentTypeId": "string",
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с вещественным documentTypeId',
            'description': '',
            'data': {
                "documentTypeId": 0.1,
                "userId": 1,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 400,
                        "userMessage": None,
                    }
                ]
            }
        },
        # TODO: разобраться с параметрами Extension и documentPackageId - пока не ясно зачем они нужны
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с несуществующим dealId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "dealId": 123123123123,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 400,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с пустым dealId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "dealId": None,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с логическим dealId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "dealId": True,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с строковым dealId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "dealId": "string",
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 0,
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Негативный тест исключительно с обязательными параметрами и с вещественным dealId',
            'description': '',
            'data': {
                "documentTypeId": 20010,
                "userId": 1,
                "dealId": 0.152,
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "code": 400,
                        "userMessage": None,
                    }
                ]
            }
        },
    ]
}

put = {}

get = {}

delete = [
    {
        'name': 'Отвязка существующего документа от сделки с проверкой возвращаемого json',
        'description': '',
        'precondition': {
            "post_doc_to_deal": {
                "documentTypeId": 20010,
                "userId": 1,
            },
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        }
    },
    {
        'name': 'Отвязка существующего документа от сделки с проверкой выставляемого флага в базе',
        'description': '',
        'precondition': {
            "post_doc_to_deal": {
                "documentTypeId": 20010,
                "userId": 1,
            },
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'sql': {
                'request': 'SELECT archived FROM deal_document WHERE deal_id=%s',
                'result': [(True,)]
            }
        }
    },
    {
        'name': 'Отвязка ранее удалённого документа от сделки',
        'description': '',
        'precondition': {
            "post_doc_to_deal": {
                "documentTypeId": 20010,
                "userId": 1,
            },
            "delete_deal": True,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        }
    },
    {
        'name': 'Отвязка несуществующего документа c ID корректного типа от сделки',
        'description': '',
        'precondition': {
            "data": {
                "id": 123123123123,
            },
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        }
    },
    {
        'name': 'Отвязка несуществующего документа c ID корректного типа от сделки',
        'description': '',
        'precondition': {
            "data": {
                "id": '40,41',
            },
            "delete_deal": False,
        },
        'data': {},
        'expected': {
            'json': {
                "success": True,
                "data": []
            }
        }
    },
]