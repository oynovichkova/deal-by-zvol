# coding=utf-8
application = {
    'phone_validation': [
        {
            'name': 'Валидный телефонный номер',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "9261304674",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER"
            },
            'expected': {
                "success": True,
                "data": [{
                    "personFirstName": "Vasya",
                    "personLastName": "Pupkin",
                    "personBirthday": "1953-04-04TZ",
                    "contactPhoneMobile": "9261304674",
                    "passportSeries": "1234",
                    "passportNumber": "567890",
                    "applicationTypePledger": False,
                    "mandatoryCoBorrower": False,
                    "applicationStatus": "DRAFT",
                    "considerCoBorrowerIncome": False,
                    "applicationType": "BORROWER"
                }]
            }
        },
        {
            'name': 'Номер телефона в международном формате',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "+79261304674",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER"
            },
            'expected': {
                "success": True,
                "data": [{
                    "personFirstName": "Vasya",
                    "personLastName": "Pupkin",
                    "personBirthday": "1953-04-04TZ",
                    "contactPhoneMobile": "9261304674",
                    "passportSeries": "1234",
                    "passportNumber": "567890",
                    "applicationTypePledger": False,
                    "mandatoryCoBorrower": False,
                    "applicationStatus": "DRAFT",
                    "considerCoBorrowerIncome": False,
                    "applicationType": "BORROWER"
                }]
            }
        },
        {
            'name': 'Длинный телефонный номер',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "79261304674",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER",
                'casId': 1,
            },
            'expected': {
                "success": False,
                "errors": [{
                    "internalMessage": 'must match \"^\\d{10}$\"'
                }]
            }
        },
        {
            'name': 'Короткий телефонный номер',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "261304674",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER",
                'casId': 1,
            },
            'expected': {
                "success": False,
                "errors": [{
                    "internalMessage": 'must match \"^\\d{10}$\"'
                }]
            }
        },
        {
            'name': 'Телефонный номер нормальной длины с символами',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "9a61304674",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER",
                'casId': 1,
            },
            'expected': {
                "success": False,
                "errors": [{
                    "internalMessage": 'must match \"^\\d{10}$\"'
                }]
            }
        },
        {
            'name': 'Пустой телефонный номер',
            'description': '',
            'data': {
                "personFirstName": "Vasya",
                "personLastName": "Pupkin",
                "personBirthday": "1953-04-04TZ",
                "contactPhoneMobile": "",
                "passportSeries": "1234",
                "passportNumber": "567890",
                "applicationTypePledger": False,
                "mandatoryCoBorrower": False,
                "applicationStatus": "DRAFT",
                "considerCoBorrowerIncome": False,
                "applicationType": "BORROWER",
                'casId': 1,
            },
            'expected': {
                "success": False,
                "errors": [{
                    "internalMessage": 'must match \"^\\d{10}$\"'
                }]
            }
        },
    ],
}

deal = {
    'deal_fields_post_validation': {
    "channelId": [
        {
            'name': 'Создание сделки с валидным ID из словаря для поля channel_id',
            'description': '',
            'data': {
                "channelId": 12020
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "channelId": 12020
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля channel_id',
            'description': '',
            'data': {
                "channelId": None
            },
            'expected': {
                "success": True,
                "data":
                    [{
                        "dealStatusId": 8060,
                        "channelId": None
                    }]
            }
        },
        {
            'name': 'Создание сделки с несуществующим ID из словаря для поля channel_id',
            'description': '',
            'data': {
                "channelId": 11111111
            },
            'expected': {
                "success": False,
                "errors":
                    [{
                        "userMessage": None,
                    }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля channel_id',
            'description': '',
            'data': {
                "channelId": 12.010
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
            'name': 'Создание сделки со строковым ID из словаря для поля channel_id',
            'description': '',
            'data': {
                "channelId": "12010"
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
    ],
    "calcId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля calc ID',
            'description': '',
            'data': {
                "calcId": 123
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "calcId": 123
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля calc ID',
            'description': '',
            'data': {
                "calcId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "calcId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля calc ID',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "calcId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля calc ID',
            'description': '',
            'data': {
                "calcId": 123.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля calc ID',
            'description': '',
            'data': {
                "calcId": "123"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
    ],
    "paymentMethodId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля paymentMethodId',
            'description': '',
            'data': {
                "paymentMethodId": 17010
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "paymentMethodId": 17010
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля paymentMethodId',
            'description': '',
            'data': {
                "paymentMethodId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "paymentMethodId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля paymentMethodId',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "paymentMethodId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля paymentMethodId',
            'description': '',
            'data': {
                "paymentMethodId": 17010.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля paymentMethodId',
            'description': '',
            'data': {
                "paymentMethodId": "17010"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
    ],
    "productTypeId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля productTypeId',
            'description': '',
            'data': {
                "productTypeId": 15050
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "productTypeId": 15050
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля productTypeId',
            'description': '',
            'data': {
                "productTypeId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "productTypeId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля productTypeId',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "productTypeId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля productTypeId',
            'description': '',
            'data': {
                "productTypeId": 15010.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля productTypeId',
            'description': '',
            'data': {
                "productTypeId": "15010"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
    ],
    "rejectionReasonId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля rejectionReasonId',
            'description': '',
            'data': {
                "rejectionReasonId": 13010
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "rejectionReasonId": 13010
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля rejectionReasonId',
            'description': '',
            'data': {
                "rejectionReasonId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "rejectionReasonId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля rejectionReasonId',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "rejectionReasonId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля rejectionReasonId',
            'description': '',
            'data': {
                "rejectionReasonId": 13010.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля rejectionReasonId',
            'description': '',
            'data': {
                "paymentMethodId": "13010"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        }
    ],
    "dealResolutionId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля dealResolutionId',
            'description': '',
            'data': {
                "dealResolutionId": 18010
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "dealResolutionId": 18010
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля dealResolutionId',
            'description': '',
            'data': {
                "dealResolutionId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "dealResolutionId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля dealResolutionId',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "dealResolutionId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля dealResolutionId',
            'description': '',
            'data': {
                "dealResolutionId": 18010.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля dealResolutionId',
            'description': '',
            'data': {
                "dealResolutionId": "18010"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
    ],
    "subproductTypeId": [
        {
            'name': 'Создание сделки с корректным значением ID для поля subproductTypeId',
            'description': '',
            'data': {
                "subproductTypeId": 16010
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "subproductTypeId": 16010
                }]
            }
        },
        {
            'name': 'Создание сделки с null для поля subproductTypeId',
            'description': '',
            'data': {
                "subproductTypeId": None
            },
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "subproductTypeId": None
                }]
            }
        },
        {
            'name': 'Создание сделки без указания значения для поля subproductTypeId',
            'description': '',
            'data': {},
            'expected': {
                "success": True,
                "data": [{
                    "dealStatusId": 8060,
                    "subproductTypeId": None
                }]
            }
        },
        {
            'name': 'Создание сделки с вещественным ID для поля subproductTypeId',
            'description': '',
            'data': {
                "subproductTypeId": 16010.5
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
        {
            'name': 'Создание сделки со строковым ID для поля subproductTypeId',
            'description': '',
            'data': {
                "subproductTypeId": "16010"
            },
            'expected': {
                "success": False,
                "errors": [
                    {
                        "userMessage": None,
                    }
                ]
            }
        },
    ]
},

    'deal_fields_put_validation': {
        "channelId": [
            {
                'name': 'Обновление сделки с null до валидного ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": None
                },
                'data': {
                    "channelId": 12020
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "channelId": 12020
                    }]
                }
            },
            {
                'name': 'Обновление сделки с валидного ID из словаря до null для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": 12010
                },
                'data': {
                    "channelId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "channelId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": 12010
                },
                'data': {
                    "channelId": 11111111
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
                'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": 12010
                },
                'data': {
                    "channelId": 12.010
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
                'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": 12010
                },
                'data': {
                    "channelId": "12010"
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
                'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": None
                },
                'data': {
                    "channelId": 11111111
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
                'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": None
                },
                'data': {
                    "channelId": 12.010
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
                'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля channel_id',
                'description': '',
                'precondition': {
                    "channelId": None
                },
                'data': {
                    "channelId": "12010"
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
        ],
        "calcId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля calc ID',
                'description': '',
                'precondition': {
                    "calcId": 123
                },
                'data': {
                    "calcId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "calcId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля calc ID',
                'description': '',
                'precondition': {},
                'data': {
                    "calcId": 123
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "calcId": 123
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля calc ID',
                'description': '',
                'precondition': {
                    "calcId": 123
                },
                'data': {
                    "calcId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "calcId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля calc ID',
                'description': '',
                'precondition': {
                    "calcId": 123
                },
                'data': {
                    "calcId": 123.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля calc ID',
                'description': '',
                'precondition': {
                    "calcId": 123
                },
                'data': {
                    "calcId": "123"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до вещественного значения ID для поля calc ID',
                'description': '',
                'precondition': {},
                'data': {
                    "calcId": 123.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до строкового значения ID для поля calc ID',
                'description': '',
                'precondition': {},
                'data': {
                    "calcId": "123"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }
        ],
        "creditAnalysysId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля creditAnalysysId',
                'description': '',
                'precondition': {
                    "creditAnalysysId": 11010
                },
                'data': {
                    "creditAnalysysId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "creditAnalysysId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля creditAnalysysId',
                'description': '',
                'precondition': {},
                'data': {
                    "creditAnalysysId": 123
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "creditAnalysysId": 11010
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля creditAnalysysId',
                'description': '',
                'precondition': {
                    "creditAnalysysId": 11010
                },
                'data': {
                    "creditAnalysysId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "creditAnalysysId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля creditAnalysysId',
                'description': '',
                'precondition': {
                    "creditAnalysysId": 11010
                },
                'data': {
                    "creditAnalysysId": 11010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля creditAnalysysId',
                'description': '',
                'precondition': {
                    "creditAnalysysId": 11010
                },
                'data': {
                    "creditAnalysysId": "11010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до вещественного значения ID для поля creditAnalysysId',
                'description': '',
                'precondition': {},
                'data': {
                    "creditAnalysysId": 11010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до строкового значения ID для поля creditAnalysysId',
                'description': '',
                'precondition': {},
                'data': {
                    "creditAnalysysId": "11010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }],
        "dealStatusId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля dealStatusId',
                'description': '',
                'precondition': {
                    "dealStatusId": 8010
                },
                'data': {
                    "dealStatusId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,

                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля dealStatusId',
                'description': '',
                'precondition': {},
                'data': {
                    "dealStatusId": 8060
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,

                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля dealStatusId',
                'description': '',
                'precondition': {
                    "dealStatusId": 8010
                },
                'data': {
                    "dealStatusId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": None,

                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля dealStatusId',
                'description': '',
                'precondition': {
                    "dealStatusId": 8010
                },
                'data': {
                    "dealStatusId": 8010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля dealStatusId',
                'description': '',
                'precondition': {
                    "dealStatusId": 8010
                },
                'data': {
                    "dealStatusId": "8010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до вещественного значения ID для поля dealStatusId',
                'description': '',
                'precondition': {},
                'data': {
                    "dealStatusId": 8010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с null до строкового значения ID для поля dealStatusId',
                'description': '',
                'precondition': {},
                'data': {
                    "dealStatusId": "8060"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }],
        "ObjectTypeId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля ObjectTypeId',
                'description': '',
                'precondition': {
                    "ObjectTypeId": 9010
                },
                'data': {
                    "ObjectTypeId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "ObjectTypeId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля ObjectTypeId',
                'description': '',
                'precondition': {},
                'data': {
                    "ObjectTypeId": 9010
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "ObjectTypeId": 9010
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля ObjectTypeId',
                'description': '',
                'precondition': {
                    "ObjectTypeId": 9010
                },
                'data': {
                    "ObjectTypeId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "ObjectTypeId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля ObjectTypeId',
                'description': '',
                'precondition': {
                    "ObjectTypeId": 9010
                },
                'data': {
                    "ObjectTypeId": 9010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля ObjectTypeId',
                'description': '',
                'precondition': {
                    "ObjectTypeId": 9010
                },
                'data': {
                    "ObjectTypeId": "9010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                },
            },
        ],
        "paymentMethodId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля paymentMethodId',
                'description': '',
                'precondition': {
                    "paymentMethodId": 17010
                },
                'data': {
                    "paymentMethodId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "paymentMethodId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля paymentMethodId',
                'description': '',
                'precondition': {},
                'data': {
                    "paymentMethodId": 17010
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "paymentMethodId": 17010
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля paymentMethodId',
                'description': '',
                'precondition': {
                    "paymentMethodId": 17010
                },
                'data': {
                    "paymentMethodId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "paymentMethodId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля paymentMethodId',
                'description': '',
                'precondition': {
                    "paymentMethodId": 17010
                },
                'data': {
                    "paymentMethodId": 17010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля paymentMethodId',
                'description': '',
                'precondition': {
                    "paymentMethodId": 17010
                },
                'data': {
                    "paymentMethodId": "17010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }],
        "productTypeId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля productTypeId',
                'description': '',
                'precondition': {
                    "productTypeId": 15010
                },
                'data': {
                    "productTypeId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "productTypeId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля productTypeId',
                'description': '',
                'precondition': {},
                'data': {
                    "productTypeId": 15010
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "productTypeId": 15010
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля productTypeId',
                'description': '',
                'precondition': {
                    "productTypeId": 15010
                },
                'data': {
                    "productTypeId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "productTypeId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля productTypeId',
                'description': '',
                'precondition': {
                    "productTypeId": 15010
                },
                'data': {
                    "productTypeId": 15010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля productTypeId',
                'description': '',
                'precondition': {
                    "productTypeId": 15010
                },
                'data': {
                    "productTypeId": "15010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }],
        "rejectionReasonId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля rejectionReasonId',
                'description': '',
                'precondition': {
                    "rejectionReasonId": 13010
                },
                'data': {
                    "rejectionReasonId": None
                },
                'expected': {
                    "success": True,
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля rejectionReasonId',
                'description': '',
                'precondition': {},
                'data': {
                    "rejectionReasonId": 13010
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "rejectionReasonId": 13010
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля rejectionReasonId',
                'description': '',
                'precondition': {
                    "rejectionReasonId": 13010
                },
                'data': {
                    "rejectionReasonId": None
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "rejectionReasonId": None
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля rejectionReasonId',
                'description': '',
                'precondition': {
                    "rejectionReasonId": 13010
                },
                'data': {
                    "rejectionReasonId": 13010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля rejectionReasonId',
                'description': '',
                'precondition': {
                    "rejectionReasonId": 13010
                },
                'data': {
                    "rejectionReasonId": "13010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }
        ],
        "dealResolutionId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля dealResolutionId',
                'description': '',
                'precondition': {
                    "dealResolutionId": 18010
                },
                'data': {
                    "dealResolutionId": None
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "dealResolutionId": None
                        }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля dealResolutionId',
                'description': '',
                'precondition': {},
                'data': {
                    "dealResolutionId": 18010
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "dealResolutionId": 18010
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля dealResolutionId',
                'description': '',
                'precondition': {
                    "dealResolutionId": 18010
                },
                'data': {
                    "dealResolutionId": None
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "dealResolutionId": None
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля dealResolutionId',
                'description': '',
                'precondition': {
                    "dealResolutionId": 18010
                },
                'data': {
                    "dealResolutionId": 18010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля dealResolutionId',
                'description': '',
                'precondition': {
                    "dealResolutionId": 18010
                },
                'data': {
                    "dealResolutionId": "18010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
        ],
        "SubProductId": [
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля SubProductId',
                'description': '',
                'precondition': {
                    "SubProductId": 16010
                },
                'data': {
                    "SubProductId": None
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "SubProductId": None
                        }]
                }
            },
            {
                'name': 'Обновление сделки с null до корректного значения ID для поля SubProductId',
                'description': '',
                'precondition': {},
                'data': {
                    "SubProductId": 16010
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "SubProductId": 16010
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до null для поля SubProductId',
                'description': '',
                'precondition': {
                    "SubProductId": 16010
                },
                'data': {
                    "SubProductId": None
                },
                'expected': {
                    "success": True,
                    "data": [
                        {
                            "dealStatusId": 8060,
                            "SubProductId": None
                        }]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до вещественного ID для поля SubProductId',
                'description': '',
                'precondition': {
                    "SubProductId": 16010
                },
                'data': {
                    "SubProductId": 16010.5
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Обновление сделки с корректным значением ID до строкового ID для поля SubProductId',
                'description': '',
                'precondition': {
                    "SubProductId": 16010
                },
                'data': {
                    "SubProductId": "16010"
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "userMessage": None,
                        }
                    ]
                }
            }
        ]
    }
}

events = {
    'events_fields_post_validation': {
        "rejectionReasonId": [
{
    'name': 'Выполнение перехода с пустым значением поля rejectionReasonId',
    'description': '',
    'data': {
        "event": "CREDIT_SENT_INTERNET"
    },
    'expected': {
        "success": True,
        "data": [{
            "rejectionReasonId": None,
        }]
    }
},
{
    'name': 'Выполнение перехода со значением null в поле rejectionReasonId',
    'description': '',
    'data': {
        "event": "CREDIT_SENT_INTERNET",
        "rejectionReasonId": None
    },
    'expected': {
        "success": True,
        "data": [{
            "rejectionReasonId": None,
        }]
    }
},
{
    'name': 'Выполнение перехода с корректным значением ID из словаря в поле rejectionReasonId',
    'description': '',
    'data': {
        "event": "CREDIT_SENT_INTERNET",
        "rejectionReasonId": 10020
    },
    'expected': {
        "success": True,
        "data": [{
            "rejectionReasonId": 10020,
        }]
    }
},
{
    'name': 'Выполнение перехода с несуществующим значением ID из словаря в поле rejectionReasonId',
    'description': '',
    'data': {
        "event": "CREDIT_SENT_INTERNET",
        "rejectionReasonId": 111111
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
    'name': 'Выполнение перехода с вещественным значением ID из словаря в поле rejectionReasonId',
    'description': '',
    'data': {
        "channelId": 10020.0
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
    'name': '',
    'description': 'Выполнение перехода с строковым значением ID из словаря в поле rejectionReasonId',
    'data': {
        "channelId": "10020"
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
],
}
}
# TODO: нужно ориентироваться не на текущее состояние, а на сосотяние, в которое переходим. Или оба
available_envs = {
    '100': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '101': ['s-101', 's-104', 's-201', 's-202'],
    '102': ['s-101', 's-104', 's-201', 's-202'],
    '103': ['s-101', 's-104', 's-201', 's-202'],
    '104': ['s-104', 's-201', 's-202'],
    '105': ['s-104', 's-201', 's-202'],
    '106': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '107': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '108': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '201': ['s-201', 's-202'],
    '202': ['s-202'],
    '203': ['s-202'],
    '204': ['s-202'],
    '301': ['s-202'],
    '302': ['s-202'],
    '401': ['s-202'],
    '402': ['s-202'],
    '001': ['s-101', 's-104', 's-201', 's-202'],
    '002': ['s-104', 's-201', 's-202'],
    '003': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '004': ['s-0', 's-101', 's-104', 's-201', 's-202'],
    '005': ['s-202'],
}
envs = [
    's-0',
    's-101',
    's-104',
    's-201',
    's-202',
]

# Данный массив нужен был при генерации тестовых данных,
# Пока закомментил, дальше нужно будет удалить
#
# available_events = [
#     "CREDIT_SENT",
#     "CREDIT_SENT",
#     "CREDIT_SENT_INTERNET",
#     "CREDIT_ACCEPTED",
#     "CREDIT_ACCEPTED_MIDDLE",
#     "CREDIT_SENT_MIDDLE",
#     "CREDIT_RETURNED_CLIENT",
#     "CREDIT_RETURNED_MIDDLE",
#     "CREDIT_RESEND",
#     "CREDIT_RESEND_CLIENT",
#     "CREDIT_CHANGED_BY_CLIENT",
#     "NOT_CREDIT_PRODUCT",
#     "CREDIT_ANALYZE",
#     "CREDIT_RETURNED",
#     "CREDIT_APPROVED",
#     "CREDIT_REJECTED",
#     "DEAL_CANCELLED_BY_CUSTOMER",
#     "BORROWER_APPROVAL_EXPIRED",
#     "DEAL_CREATED",
#     "ESTATE_CANCELLED",
#     "BORROWER_APPROVED",
#     "AGENCY_SELECTED",
#     "ESTATE_DOCUMENTS_SENT",
#     "CLIENT_ALREADY_HAS_ESTATE",
#     "REFINANCING",
#     "ESTATE_REJECTED",
#     "CLIENT_REJECTED_AGENCY",
#     "ESTATE_DOCUMENTS_RETURNED",
#     "ESTATE_LOST",
#     "LEAD_ACCEPTED",
#     "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER",
#     "ESTATE_DOCUMENTS_SENT_BY_AGENT",
#     "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT",
#     "ESTATE_FROM_AGENT_REJECTED",
#     "ESTATE_APPROVED_WITH_CONDITIONS_RESALE",
#     "ESTATE_APPROVED_RESALE",
#     "ESTATE_APPROVED_PRIMARY",
#     "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY",
#     "BORROWER_REJECTED",
#     "ROSREESTR_REGISTRATION_STARTED",
#     "ESTATE_BOUGHT_NOTIFICATION",
# ]

ddt_set = [
    {"state": "104", "event": "CREDIT_SENT", "result": False},
    {"state": "104", "event": "CREDIT_SENT", "result": False},
    {"state": "104", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "104", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "104", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "104", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "104", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "104", "event": "CREDIT_RETURNED_MIDDLE", "result": True},
    {"state": "104", "event": "CREDIT_RESEND", "result": False},
    {"state": "104", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "104", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "104", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "104", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "104", "event": "CREDIT_RETURNED", "result": True},
    {"state": "104", "event": "CREDIT_APPROVED", "result": True},
    {"state": "104", "event": "CREDIT_REJECTED", "result": True},
    {"state": "104", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "104", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "104", "event": "DEAL_CREATED", "result": False},
    {"state": "104", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "104", "event": "BORROWER_APPROVED", "result": False},
    {"state": "104", "event": "AGENCY_SELECTED", "result": False},
    {"state": "104", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "104", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "104", "event": "REFINANCING", "result": False},
    {"state": "104", "event": "ESTATE_REJECTED", "result": False},
    {"state": "104", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "104", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "104", "event": "ESTATE_LOST", "result": False},
    {"state": "104", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "104", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "104", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "104", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "104", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "104", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "104", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "104", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "104", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "104", "event": "BORROWER_REJECTED", "result": False},
    {"state": "104", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "104", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "100", "event": "CREDIT_SENT", "result": True},
    {"state": "100", "event": "CREDIT_SENT_INTERNET", "result": True},
    {"state": "100", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "100", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "100", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "100", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "100", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "100", "event": "CREDIT_RESEND", "result": False},
    {"state": "100", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "100", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "100", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "100", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "100", "event": "CREDIT_RETURNED", "result": False},
    {"state": "100", "event": "CREDIT_APPROVED", "result": False},
    {"state": "100", "event": "CREDIT_REJECTED", "result": False},
    {"state": "100", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "100", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "100", "event": "DEAL_CREATED", "result": False},
    {"state": "100", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "100", "event": "BORROWER_APPROVED", "result": False},
    {"state": "100", "event": "AGENCY_SELECTED", "result": False},
    {"state": "100", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "100", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "100", "event": "REFINANCING", "result": False},
    {"state": "100", "event": "ESTATE_REJECTED", "result": False},
    {"state": "100", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "100", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "100", "event": "ESTATE_LOST", "result": False},
    {"state": "100", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "100", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "100", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "100", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "100", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "100", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "100", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "100", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "100", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "100", "event": "BORROWER_REJECTED", "result": False},
    {"state": "100", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "100", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "106", "event": "CREDIT_SENT", "result": False},
    {"state": "106", "event": "CREDIT_SENT", "result": False},
    {"state": "106", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "106", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "106", "event": "CREDIT_ACCEPTED_MIDDLE", "result": True},
    {"state": "106", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "106", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "106", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "106", "event": "CREDIT_RESEND", "result": False},
    {"state": "106", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "106", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "106", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "106", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "106", "event": "CREDIT_RETURNED", "result": False},
    {"state": "106", "event": "CREDIT_APPROVED", "result": False},
    {"state": "106", "event": "CREDIT_REJECTED", "result": False},
    {"state": "106", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "106", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "106", "event": "DEAL_CREATED", "result": False},
    {"state": "106", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "106", "event": "BORROWER_APPROVED", "result": False},
    {"state": "106", "event": "AGENCY_SELECTED", "result": False},
    {"state": "106", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "106", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "106", "event": "REFINANCING", "result": False},
    {"state": "106", "event": "ESTATE_REJECTED", "result": False},
    {"state": "106", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "106", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "106", "event": "ESTATE_LOST", "result": False},
    {"state": "106", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "106", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "106", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "106", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "106", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "106", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "106", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "106", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "106", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "106", "event": "BORROWER_REJECTED", "result": False},
    {"state": "106", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "106", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "402", "event": "CREDIT_SENT", "result": False},
    {"state": "402", "event": "CREDIT_SENT", "result": False},
    {"state": "402", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "402", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "402", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "402", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "402", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "402", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "402", "event": "CREDIT_RESEND", "result": False},
    {"state": "402", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "402", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "402", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "402", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "402", "event": "CREDIT_RETURNED", "result": False},
    {"state": "402", "event": "CREDIT_APPROVED", "result": False},
    {"state": "402", "event": "CREDIT_REJECTED", "result": False},
    {"state": "402", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "402", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "402", "event": "DEAL_CREATED", "result": False},
    {"state": "402", "event": "ESTATE_CANCELLED", "result": True},
    {"state": "402", "event": "BORROWER_APPROVED", "result": False},
    {"state": "402", "event": "AGENCY_SELECTED", "result": False},
    {"state": "402", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "402", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "402", "event": "REFINANCING", "result": False},
    {"state": "402", "event": "ESTATE_REJECTED", "result": False},
    {"state": "402", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "402", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "402", "event": "ESTATE_LOST", "result": False},
    {"state": "402", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "402", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "402", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "402", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "402", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "402", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "402", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "402", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "402", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "402", "event": "BORROWER_REJECTED", "result": False},
    {"state": "402", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "402", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": True},
    {"state": "108", "event": "CREDIT_SENT", "result": False},
    {"state": "108", "event": "CREDIT_SENT", "result": False},
    {"state": "108", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "108", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "108", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "108", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "108", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "108", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "108", "event": "CREDIT_RESEND", "result": False},
    {"state": "108", "event": "CREDIT_RESEND_CLIENT", "result": True},
    {"state": "108", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "108", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "108", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "108", "event": "CREDIT_RETURNED", "result": False},
    {"state": "108", "event": "CREDIT_APPROVED", "result": False},
    {"state": "108", "event": "CREDIT_REJECTED", "result": False},
    {"state": "108", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "108", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "108", "event": "DEAL_CREATED", "result": False},
    {"state": "108", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "108", "event": "BORROWER_APPROVED", "result": False},
    {"state": "108", "event": "AGENCY_SELECTED", "result": False},
    {"state": "108", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "108", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "108", "event": "REFINANCING", "result": False},
    {"state": "108", "event": "ESTATE_REJECTED", "result": False},
    {"state": "108", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "108", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "108", "event": "ESTATE_LOST", "result": False},
    {"state": "108", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "108", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "108", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "108", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "108", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "108", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "108", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "108", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "108", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "108", "event": "BORROWER_REJECTED", "result": False},
    {"state": "108", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "108", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "003", "event": "CREDIT_SENT", "result": False},
    {"state": "003", "event": "CREDIT_SENT", "result": False},
    {"state": "003", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "003", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "003", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "003", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "003", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "003", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "003", "event": "CREDIT_RESEND", "result": False},
    {"state": "003", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "003", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "003", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "003", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "003", "event": "CREDIT_RETURNED", "result": False},
    {"state": "003", "event": "CREDIT_APPROVED", "result": False},
    {"state": "003", "event": "CREDIT_REJECTED", "result": False},
    {"state": "003", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": False},
    {"state": "003", "event": "BORROWER_APPROVAL_EXPIRED", "result": False},
    {"state": "003", "event": "DEAL_CREATED", "result": False},
    {"state": "003", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "003", "event": "BORROWER_APPROVED", "result": False},
    {"state": "003", "event": "AGENCY_SELECTED", "result": False},
    {"state": "003", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "003", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "003", "event": "REFINANCING", "result": False},
    {"state": "003", "event": "ESTATE_REJECTED", "result": False},
    {"state": "003", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "003", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "003", "event": "ESTATE_LOST", "result": False},
    {"state": "003", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "003", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "003", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "003", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "003", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "003", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "003", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "003", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "003", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "003", "event": "BORROWER_REJECTED", "result": False},
    {"state": "003", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "003", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "102", "event": "CREDIT_SENT", "result": False},
    {"state": "102", "event": "CREDIT_SENT", "result": False},
    {"state": "102", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "102", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "102", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "102", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "102", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "102", "event": "CREDIT_RETURNED_MIDDLE", "result": True},
    {"state": "102", "event": "CREDIT_RESEND", "result": False},
    {"state": "102", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "102", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "102", "event": "NOT_CREDIT_PRODUCT", "result": True},
    {"state": "102", "event": "CREDIT_ANALYZE", "result": True},
    {"state": "102", "event": "CREDIT_RETURNED", "result": True},
    {"state": "102", "event": "CREDIT_APPROVED", "result": False},
    {"state": "102", "event": "CREDIT_REJECTED", "result": False},
    {"state": "102", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "102", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "102", "event": "DEAL_CREATED", "result": False},
    {"state": "102", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "102", "event": "BORROWER_APPROVED", "result": False},
    {"state": "102", "event": "AGENCY_SELECTED", "result": False},
    {"state": "102", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "102", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "102", "event": "REFINANCING", "result": False},
    {"state": "102", "event": "ESTATE_REJECTED", "result": False},
    {"state": "102", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "102", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "102", "event": "ESTATE_LOST", "result": False},
    {"state": "102", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "102", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "102", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "102", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "102", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "102", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "102", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "102", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "102", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "102", "event": "BORROWER_REJECTED", "result": False},
    {"state": "102", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "102", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "302", "event": "CREDIT_SENT", "result": False},
    {"state": "302", "event": "CREDIT_SENT", "result": False},
    {"state": "302", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "302", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "302", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "302", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "302", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "302", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "302", "event": "CREDIT_RESEND", "result": False},
    {"state": "302", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "302", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "302", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "302", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "302", "event": "CREDIT_RETURNED", "result": False},
    {"state": "302", "event": "CREDIT_APPROVED", "result": False},
    {"state": "302", "event": "CREDIT_REJECTED", "result": False},
    {"state": "302", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "302", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "302", "event": "DEAL_CREATED", "result": False},
    {"state": "302", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "302", "event": "BORROWER_APPROVED", "result": False},
    {"state": "302", "event": "AGENCY_SELECTED", "result": False},
    {"state": "302", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "302", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "302", "event": "REFINANCING", "result": False},
    {"state": "302", "event": "ESTATE_REJECTED", "result": False},
    {"state": "302", "event": "CLIENT_REJECTED_AGENCY", "result": True},
    {"state": "302", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "302", "event": "ESTATE_LOST", "result": False},
    {"state": "302", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "302", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "302", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": True},
    {"state": "302", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "302", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "302", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "302", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "302", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "302", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "302", "event": "BORROWER_REJECTED", "result": False},
    {"state": "302", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "302", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "107", "event": "CREDIT_SENT", "result": False},
    {"state": "107", "event": "CREDIT_SENT", "result": False},
    {"state": "107", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "107", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "107", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "107", "event": "CREDIT_SENT_MIDDLE", "result": True},
    {"state": "107", "event": "CREDIT_RETURNED_CLIENT", "result": True},
    {"state": "107", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "107", "event": "CREDIT_RESEND", "result": False},
    {"state": "107", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "107", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "107", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "107", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "107", "event": "CREDIT_RETURNED", "result": False},
    {"state": "107", "event": "CREDIT_APPROVED", "result": False},
    {"state": "107", "event": "CREDIT_REJECTED", "result": False},
    {"state": "107", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "107", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "107", "event": "DEAL_CREATED", "result": False},
    {"state": "107", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "107", "event": "BORROWER_APPROVED", "result": False},
    {"state": "107", "event": "AGENCY_SELECTED", "result": False},
    {"state": "107", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "107", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "107", "event": "REFINANCING", "result": False},
    {"state": "107", "event": "ESTATE_REJECTED", "result": False},
    {"state": "107", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "107", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "107", "event": "ESTATE_LOST", "result": False},
    {"state": "107", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "107", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "107", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "107", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "107", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "107", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "107", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "107", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "107", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "107", "event": "BORROWER_REJECTED", "result": False},
    {"state": "107", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "107", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "203", "event": "CREDIT_SENT", "result": False},
    {"state": "203", "event": "CREDIT_SENT", "result": False},
    {"state": "203", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "203", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "203", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "203", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "203", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "203", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "203", "event": "CREDIT_RESEND", "result": False},
    {"state": "203", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "203", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "203", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "203", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "203", "event": "CREDIT_RETURNED", "result": False},
    {"state": "203", "event": "CREDIT_APPROVED", "result": False},
    {"state": "203", "event": "CREDIT_REJECTED", "result": False},
    {"state": "203", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "203", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "203", "event": "DEAL_CREATED", "result": False},
    {"state": "203", "event": "ESTATE_CANCELLED", "result": True},
    {"state": "203", "event": "BORROWER_APPROVED", "result": False},
    {"state": "203", "event": "AGENCY_SELECTED", "result": False},
    {"state": "203", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "203", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "203", "event": "REFINANCING", "result": False},
    {"state": "203", "event": "ESTATE_REJECTED", "result": False},
    {"state": "203", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "203", "event": "ESTATE_DOCUMENTS_RETURNED", "result": True},
    {"state": "203", "event": "ESTATE_LOST", "result": True},
    {"state": "203", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "203", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": True},
    {"state": "203", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "203", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": True},
    {"state": "203", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "203", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "203", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "203", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "203", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "203", "event": "BORROWER_REJECTED", "result": False},
    {"state": "203", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "203", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "105", "event": "CREDIT_SENT", "result": False},
    {"state": "105", "event": "CREDIT_SENT", "result": False},
    {"state": "105", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "105", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "105", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "105", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "105", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "105", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "105", "event": "CREDIT_RESEND", "result": False},
    {"state": "105", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "105", "event": "CREDIT_CHANGED_BY_CLIENT", "result": True},
    {"state": "105", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "105", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "105", "event": "CREDIT_RETURNED", "result": False},
    {"state": "105", "event": "CREDIT_APPROVED", "result": False},
    {"state": "105", "event": "CREDIT_REJECTED", "result": True},
    {"state": "105", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "105", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "105", "event": "DEAL_CREATED", "result": True},
    {"state": "105", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "105", "event": "BORROWER_APPROVED", "result": False},
    {"state": "105", "event": "AGENCY_SELECTED", "result": False},
    {"state": "105", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "105", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "105", "event": "REFINANCING", "result": False},
    {"state": "105", "event": "ESTATE_REJECTED", "result": False},
    {"state": "105", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "105", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "105", "event": "ESTATE_LOST", "result": False},
    {"state": "105", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "105", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "105", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "105", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "105", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "105", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "105", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "105", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "105", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "105", "event": "BORROWER_REJECTED", "result": False},
    {"state": "105", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "105", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "103", "event": "CREDIT_SENT", "result": False},
    {"state": "103", "event": "CREDIT_SENT", "result": False},
    {"state": "103", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "103", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "103", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "103", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "103", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "103", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "103", "event": "CREDIT_RESEND", "result": True},
    {"state": "103", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "103", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "103", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "103", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "103", "event": "CREDIT_RETURNED", "result": False},
    {"state": "103", "event": "CREDIT_APPROVED", "result": False},
    {"state": "103", "event": "CREDIT_REJECTED", "result": False},
    {"state": "103", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "103", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "103", "event": "DEAL_CREATED", "result": False},
    {"state": "103", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "103", "event": "BORROWER_APPROVED", "result": False},
    {"state": "103", "event": "AGENCY_SELECTED", "result": False},
    {"state": "103", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "103", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "103", "event": "REFINANCING", "result": False},
    {"state": "103", "event": "ESTATE_REJECTED", "result": False},
    {"state": "103", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "103", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "103", "event": "ESTATE_LOST", "result": False},
    {"state": "103", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "103", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "103", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "103", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "103", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "103", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "103", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "103", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "103", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "103", "event": "BORROWER_REJECTED", "result": False},
    {"state": "103", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "103", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "202", "event": "CREDIT_SENT", "result": False},
    {"state": "202", "event": "CREDIT_SENT", "result": False},
    {"state": "202", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "202", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "202", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "202", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "202", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "202", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "202", "event": "CREDIT_RESEND", "result": False},
    {"state": "202", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "202", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "202", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "202", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "202", "event": "CREDIT_RETURNED", "result": False},
    {"state": "202", "event": "CREDIT_APPROVED", "result": False},
    {"state": "202", "event": "CREDIT_REJECTED", "result": False},
    {"state": "202", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "202", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "202", "event": "DEAL_CREATED", "result": False},
    {"state": "202", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "202", "event": "BORROWER_APPROVED", "result": False},
    {"state": "202", "event": "AGENCY_SELECTED", "result": True},
    {"state": "202", "event": "ESTATE_DOCUMENTS_SENT", "result": True},
    {"state": "202", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": True},
    {"state": "202", "event": "REFINANCING", "result": True},
    {"state": "202", "event": "ESTATE_REJECTED", "result": False},
    {"state": "202", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "202", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "202", "event": "ESTATE_LOST", "result": False},
    {"state": "202", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "202", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "202", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "202", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "202", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "202", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "202", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "202", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "202", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "202", "event": "BORROWER_REJECTED", "result": False},
    {"state": "202", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "202", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "004", "event": "CREDIT_SENT", "result": False},
    {"state": "004", "event": "CREDIT_SENT", "result": False},
    {"state": "004", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "004", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "004", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "004", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "004", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "004", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "004", "event": "CREDIT_RESEND", "result": False},
    {"state": "004", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "004", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "004", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "004", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "004", "event": "CREDIT_RETURNED", "result": False},
    {"state": "004", "event": "CREDIT_APPROVED", "result": False},
    {"state": "004", "event": "CREDIT_REJECTED", "result": False},
    {"state": "004", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": False},
    {"state": "004", "event": "BORROWER_APPROVAL_EXPIRED", "result": False},
    {"state": "004", "event": "DEAL_CREATED", "result": False},
    {"state": "004", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "004", "event": "BORROWER_APPROVED", "result": False},
    {"state": "004", "event": "AGENCY_SELECTED", "result": False},
    {"state": "004", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "004", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "004", "event": "REFINANCING", "result": False},
    {"state": "004", "event": "ESTATE_REJECTED", "result": False},
    {"state": "004", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "004", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "004", "event": "ESTATE_LOST", "result": False},
    {"state": "004", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "004", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "004", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "004", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "004", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "004", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "004", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "004", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "004", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "004", "event": "BORROWER_REJECTED", "result": False},
    {"state": "004", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "004", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "401", "event": "CREDIT_SENT", "result": False},
    {"state": "401", "event": "CREDIT_SENT", "result": False},
    {"state": "401", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "401", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "401", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "401", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "401", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "401", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "401", "event": "CREDIT_RESEND", "result": False},
    {"state": "401", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "401", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "401", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "401", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "401", "event": "CREDIT_RETURNED", "result": False},
    {"state": "401", "event": "CREDIT_APPROVED", "result": False},
    {"state": "401", "event": "CREDIT_REJECTED", "result": False},
    {"state": "401", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "401", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "401", "event": "DEAL_CREATED", "result": False},
    {"state": "401", "event": "ESTATE_CANCELLED", "result": True},
    {"state": "401", "event": "BORROWER_APPROVED", "result": False},
    {"state": "401", "event": "AGENCY_SELECTED", "result": False},
    {"state": "401", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "401", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "401", "event": "REFINANCING", "result": False},
    {"state": "401", "event": "ESTATE_REJECTED", "result": False},
    {"state": "401", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "401", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "401", "event": "ESTATE_LOST", "result": False},
    {"state": "401", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "401", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "401", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "401", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "401", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "401", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "401", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "401", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "401", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "401", "event": "BORROWER_REJECTED", "result": False},
    {"state": "401", "event": "ROSREESTR_REGISTRATION_STARTED", "result": True},
    {"state": "401", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "204", "event": "CREDIT_SENT", "result": False},
    {"state": "204", "event": "CREDIT_SENT", "result": False},
    {"state": "204", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "204", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "204", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "204", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "204", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "204", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "204", "event": "CREDIT_RESEND", "result": False},
    {"state": "204", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "204", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "204", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "204", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "204", "event": "CREDIT_RETURNED", "result": False},
    {"state": "204", "event": "CREDIT_APPROVED", "result": False},
    {"state": "204", "event": "CREDIT_REJECTED", "result": False},
    {"state": "204", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "204", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "204", "event": "DEAL_CREATED", "result": False},
    {"state": "204", "event": "ESTATE_CANCELLED", "result": True},
    {"state": "204", "event": "BORROWER_APPROVED", "result": False},
    {"state": "204", "event": "AGENCY_SELECTED", "result": False},
    {"state": "204", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "204", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "204", "event": "REFINANCING", "result": False},
    {"state": "204", "event": "ESTATE_REJECTED", "result": True},
    {"state": "204", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "204", "event": "ESTATE_DOCUMENTS_RETURNED", "result": True},
    {"state": "204", "event": "ESTATE_LOST", "result": False},
    {"state": "204", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "204", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "204", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "204", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": True},
    {"state": "204", "event": "ESTATE_FROM_AGENT_REJECTED", "result": True},
    {"state": "204", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": True},
    {"state": "204", "event": "ESTATE_APPROVED_RESALE", "result": True},
    {"state": "204", "event": "ESTATE_APPROVED_PRIMARY", "result": True},
    {"state": "204", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": True},
    {"state": "204", "event": "BORROWER_REJECTED", "result": True},
    {"state": "204", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "204", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "005", "event": "CREDIT_SENT", "result": False},
    {"state": "005", "event": "CREDIT_SENT", "result": False},
    {"state": "005", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "005", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "005", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "005", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "005", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "005", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "005", "event": "CREDIT_RESEND", "result": False},
    {"state": "005", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "005", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "005", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "005", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "005", "event": "CREDIT_RETURNED", "result": False},
    {"state": "005", "event": "CREDIT_APPROVED", "result": False},
    {"state": "005", "event": "CREDIT_REJECTED", "result": False},
    {"state": "005", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": False},
    {"state": "005", "event": "BORROWER_APPROVAL_EXPIRED", "result": False},
    {"state": "005", "event": "DEAL_CREATED", "result": False},
    {"state": "005", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "005", "event": "BORROWER_APPROVED", "result": False},
    {"state": "005", "event": "AGENCY_SELECTED", "result": False},
    {"state": "005", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "005", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "005", "event": "REFINANCING", "result": False},
    {"state": "005", "event": "ESTATE_REJECTED", "result": False},
    {"state": "005", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "005", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "005", "event": "ESTATE_LOST", "result": False},
    {"state": "005", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "005", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "005", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "005", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "005", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "005", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "005", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "005", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "005", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "005", "event": "BORROWER_REJECTED", "result": False},
    {"state": "005", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "005", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "001", "event": "CREDIT_SENT", "result": False},
    {"state": "001", "event": "CREDIT_SENT", "result": False},
    {"state": "001", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "001", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "001", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "001", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "001", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "001", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "001", "event": "CREDIT_RESEND", "result": False},
    {"state": "001", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "001", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "001", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "001", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "001", "event": "CREDIT_RETURNED", "result": False},
    {"state": "001", "event": "CREDIT_APPROVED", "result": False},
    {"state": "001", "event": "CREDIT_REJECTED", "result": False},
    {"state": "001", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": False},
    {"state": "001", "event": "BORROWER_APPROVAL_EXPIRED", "result": False},
    {"state": "001", "event": "DEAL_CREATED", "result": False},
    {"state": "001", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "001", "event": "BORROWER_APPROVED", "result": False},
    {"state": "001", "event": "AGENCY_SELECTED", "result": False},
    {"state": "001", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "001", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "001", "event": "REFINANCING", "result": False},
    {"state": "001", "event": "ESTATE_REJECTED", "result": False},
    {"state": "001", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "001", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "001", "event": "ESTATE_LOST", "result": False},
    {"state": "001", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "001", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "001", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "001", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "001", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "001", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "001", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "001", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "001", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "001", "event": "BORROWER_REJECTED", "result": False},
    {"state": "001", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "001", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "101", "event": "CREDIT_SENT", "result": False},
    {"state": "101", "event": "CREDIT_SENT", "result": False},
    {"state": "101", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "101", "event": "CREDIT_ACCEPTED", "result": True},
    {"state": "101", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "101", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "101", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "101", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "101", "event": "CREDIT_RESEND", "result": False},
    {"state": "101", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "101", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "101", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "101", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "101", "event": "CREDIT_RETURNED", "result": False},
    {"state": "101", "event": "CREDIT_APPROVED", "result": False},
    {"state": "101", "event": "CREDIT_REJECTED", "result": False},
    {"state": "101", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "101", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "101", "event": "DEAL_CREATED", "result": False},
    {"state": "101", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "101", "event": "BORROWER_APPROVED", "result": False},
    {"state": "101", "event": "AGENCY_SELECTED", "result": False},
    {"state": "101", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "101", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "101", "event": "REFINANCING", "result": False},
    {"state": "101", "event": "ESTATE_REJECTED", "result": False},
    {"state": "101", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "101", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "101", "event": "ESTATE_LOST", "result": False},
    {"state": "101", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "101", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "101", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "101", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "101", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "101", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "101", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "101", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "101", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "101", "event": "BORROWER_REJECTED", "result": False},
    {"state": "101", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "101", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "201", "event": "CREDIT_SENT", "result": False},
    {"state": "201", "event": "CREDIT_SENT", "result": False},
    {"state": "201", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "201", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "201", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "201", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "201", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "201", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "201", "event": "CREDIT_RESEND", "result": False},
    {"state": "201", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "201", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "201", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "201", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "201", "event": "CREDIT_RETURNED", "result": False},
    {"state": "201", "event": "CREDIT_APPROVED", "result": False},
    {"state": "201", "event": "CREDIT_REJECTED", "result": False},
    {"state": "201", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "201", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "201", "event": "DEAL_CREATED", "result": False},
    {"state": "201", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "201", "event": "BORROWER_APPROVED", "result": True},
    {"state": "201", "event": "AGENCY_SELECTED", "result": False},
    {"state": "201", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "201", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "201", "event": "REFINANCING", "result": False},
    {"state": "201", "event": "ESTATE_REJECTED", "result": False},
    {"state": "201", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "201", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "201", "event": "ESTATE_LOST", "result": False},
    {"state": "201", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "201", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "201", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "201", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "201", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "201", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "201", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "201", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "201", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "201", "event": "BORROWER_REJECTED", "result": False},
    {"state": "201", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "201", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "002", "event": "CREDIT_SENT", "result": False},
    {"state": "002", "event": "CREDIT_SENT", "result": False},
    {"state": "002", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "002", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "002", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "002", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "002", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "002", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "002", "event": "CREDIT_RESEND", "result": False},
    {"state": "002", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "002", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "002", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "002", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "002", "event": "CREDIT_RETURNED", "result": False},
    {"state": "002", "event": "CREDIT_APPROVED", "result": False},
    {"state": "002", "event": "CREDIT_REJECTED", "result": False},
    {"state": "002", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": False},
    {"state": "002", "event": "BORROWER_APPROVAL_EXPIRED", "result": False},
    {"state": "002", "event": "DEAL_CREATED", "result": False},
    {"state": "002", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "002", "event": "BORROWER_APPROVED", "result": False},
    {"state": "002", "event": "AGENCY_SELECTED", "result": False},
    {"state": "002", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "002", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "002", "event": "REFINANCING", "result": False},
    {"state": "002", "event": "ESTATE_REJECTED", "result": False},
    {"state": "002", "event": "CLIENT_REJECTED_AGENCY", "result": False},
    {"state": "002", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "002", "event": "ESTATE_LOST", "result": False},
    {"state": "002", "event": "LEAD_ACCEPTED", "result": False},
    {"state": "002", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "002", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "002", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "002", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "002", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "002", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "002", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "002", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "002", "event": "BORROWER_REJECTED", "result": False},
    {"state": "002", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "002", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
    {"state": "301", "event": "CREDIT_SENT", "result": False},
    {"state": "301", "event": "CREDIT_SENT", "result": False},
    {"state": "301", "event": "CREDIT_SENT_INTERNET", "result": False},
    {"state": "301", "event": "CREDIT_ACCEPTED", "result": False},
    {"state": "301", "event": "CREDIT_ACCEPTED_MIDDLE", "result": False},
    {"state": "301", "event": "CREDIT_SENT_MIDDLE", "result": False},
    {"state": "301", "event": "CREDIT_RETURNED_CLIENT", "result": False},
    {"state": "301", "event": "CREDIT_RETURNED_MIDDLE", "result": False},
    {"state": "301", "event": "CREDIT_RESEND", "result": False},
    {"state": "301", "event": "CREDIT_RESEND_CLIENT", "result": False},
    {"state": "301", "event": "CREDIT_CHANGED_BY_CLIENT", "result": False},
    {"state": "301", "event": "NOT_CREDIT_PRODUCT", "result": False},
    {"state": "301", "event": "CREDIT_ANALYZE", "result": False},
    {"state": "301", "event": "CREDIT_RETURNED", "result": False},
    {"state": "301", "event": "CREDIT_APPROVED", "result": False},
    {"state": "301", "event": "CREDIT_REJECTED", "result": False},
    {"state": "301", "event": "DEAL_CANCELLED_BY_CUSTOMER", "result": True},
    {"state": "301", "event": "BORROWER_APPROVAL_EXPIRED", "result": True},
    {"state": "301", "event": "DEAL_CREATED", "result": False},
    {"state": "301", "event": "ESTATE_CANCELLED", "result": False},
    {"state": "301", "event": "BORROWER_APPROVED", "result": False},
    {"state": "301", "event": "AGENCY_SELECTED", "result": False},
    {"state": "301", "event": "ESTATE_DOCUMENTS_SENT", "result": False},
    {"state": "301", "event": "CLIENT_ALREADY_HAS_ESTATE", "result": False},
    {"state": "301", "event": "REFINANCING", "result": False},
    {"state": "301", "event": "ESTATE_REJECTED", "result": False},
    {"state": "301", "event": "CLIENT_REJECTED_AGENCY", "result": True},
    {"state": "301", "event": "ESTATE_DOCUMENTS_RETURNED", "result": False},
    {"state": "301", "event": "ESTATE_LOST", "result": False},
    {"state": "301", "event": "LEAD_ACCEPTED", "result": True},
    {"state": "301", "event": "ESTATE_DOCUMENTS_ACCEPTED_BY_MANAGER", "result": False},
    {"state": "301", "event": "ESTATE_DOCUMENTS_SENT_BY_AGENT", "result": False},
    {"state": "301", "event": "ESTATE_DOCUMENTS_RETURNED_FROM_AGENT", "result": False},
    {"state": "301", "event": "ESTATE_FROM_AGENT_REJECTED", "result": False},
    {"state": "301", "event": "ESTATE_APPROVED_WITH_CONDITIONS_RESALE", "result": False},
    {"state": "301", "event": "ESTATE_APPROVED_RESALE", "result": False},
    {"state": "301", "event": "ESTATE_APPROVED_PRIMARY", "result": False},
    {"state": "301", "event": "ESTATE_APPROVED_WITH_CONDITIONS_PRIMARY", "result": False},
    {"state": "301", "event": "BORROWER_REJECTED", "result": False},
    {"state": "301", "event": "ROSREESTR_REGISTRATION_STARTED", "result": False},
    {"state": "301", "event": "ESTATE_BOUGHT_NOTIFICATION", "result": False},
]