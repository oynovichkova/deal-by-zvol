# coding=utf-8

deal = {
    'deal_fields_post_validation':
        {"createdTime": [
            {
                'name': 'Валидная дата создания сделки для поля createdTime',
                'description': 'Дата создания сущности валидная',
                'data': {
                    "createdTime": '12.12.2016'
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "createdTime": '12.12.2016'
                    }]
                }
            },

            {
                'name': 'Невалидная дата из будущего создания сделки для поля createdTime',
                'description': 'Дата создания сущности невалидная',
                'data': {
                    "createdTime": '12.12.2017'
                },
                'expected': {
                    "success": False,
                    "data": [{
                        "dealStatusId": 8060,
                        "createdTime": '12.12.2017'
                    }]
                }
            },
            {
                'name': 'Невалидная дата None создания сделки для поля createdTime',
                'description': 'Дата создания сущности пустая',
                'data': {
                    "createdTime": None
                },
                'expected': {
                    "success": False,
                    "data": [{
                        "dealStatusId": 8060,
                        "createdTime": None
                    }]
                }
            },
            {
                'name': 'Невалидная пустая дата создания сделки для поля createdTime',
                'description': 'Дата создания сущности пустая',
                'data': {
                    "createdTime": ''
                },
                'expected': {
                    "success": False,
                    "data": [{
                        "dealStatusId": 8060,
                        "createdTime": ''
                    }]
                }
            },
        ],
            "dealId": [
                {
                    'name': 'Создание валидной сделки для поля dealId, где id еще не существует',
                    'description': '',
                    'data': {
                        "dealId": 1001
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Создание невалидной сделки для поля dealId, где id уже существует',
                    'description': '',
                    'data': {
                        "dealId": 534
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
                    'name': 'Создание невалидной сделки для поля dealId, где id None',
                    'description': '',
                    'data': {
                        "dealId": None
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
                    'name': 'Создание невалидной сделки для поля dealId, где id пусто',
                    'description': '',
                    'data': {
                        "dealId": ''
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
            "casId": [
                {
                    'name': 'валидный несуществующий кас айди создания сделки для поля casId',
                    'description': '',
                    'data': {
                        "casId": 400000
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": 400000
                        }]
                    }
                },
                {
                    'name': 'невалидный существующий кас айди создания сделки для поля casId',
                    'description': '',
                    'data': {
                        "casId": 4
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": 4
                        }]
                    }
                },
                {
                    'name': 'невалидный пустой кас айди создания сделки для поля casId',
                    'description': '',
                    'data': {
                        "casId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": ''
                        }]
                    }
                },
                {
                    'name': 'невалидный несуществующий кас айди создания сделки для поля casId',
                    'description': '',
                    'data': {
                        "casId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": None
                        }]
                    }
                },

            ],
            "actNumber": [
                {
                    'name': ' валидный номер акта приема - передачи дел клиентов от партнера в банк',
                    'description': '',
                    'data': {
                        "actNumber": 'a090909'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "actNumber": 'a090909'
                        }]
                    }
                },
                {
                    'name': ' не валидный номер акта приема - передачи дел клиентов от партнера в банк',
                    'description': '',
                    'data': {
                        "actNumber": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "actNumber": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный номер акта приема - передачи дел клиентов от партнера в банк',
                    'description': '',
                    'data': {
                        "actNumber": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "actNumber": None
                        }]
                    }
                }

            ],
            "additionalInfo": [
                {
                    'name': 'валиднное поле Доп.инфо',
                    'description': '',
                    'data': {
                        "additionalInfo": 'Строка. 5.;99 Cyrillic'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": 'Строка. 5.;99 Cyrillic'
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Доп.инфо',
                    'description': '',
                    'data': {
                        "additionalInfo": 1678
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": 1678
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Доп.инфо',
                    'description': '',
                    'data': {
                        "additionalInfo": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Доп.инфо',
                    'description': '',
                    'data': {
                        "additionalInfo": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": None
                        }]
                    }
                }
            ],
            "agreementDocument": [
                {
                    'name': 'валиднное поле Cсылка на кредитный договор',
                    'description': '',
                    'data': {
                        "agreementDocument": 1243343
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": 1243343
                        }]
                    }
                },
                {
                    'name': 'Не валиднное поле Cсылка на кредитный договор',
                    'description': '',
                    'data': {
                        "agreementDocument": 1.979
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": 1.979
                        }]
                    }
                },
                {
                    'name': 'Не валиднное поле Cсылка на кредитный договор',
                    'description': '',
                    'data': {
                        "agreementDocument": 'Строка. 5.;99 Cyrillic'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": 'Строка. 5.;99 Cyrillic'
                        }]
                    }
                },
                {
                    'name': 'Не валиднное поле Cсылка на кредитный договор',
                    'description': '',
                    'data': {
                        "agreementDocument": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": ''
                        }]
                    }
                },
                {
                    'name': 'Не валиднное поле Cсылка на кредитный договор',
                    'description': '',
                    'data': {
                        "agreementDocument": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": None
                        }]
                    }
                },
            ],
            "approvalPartnerOfficeId": [
                {
                    'name': 'валиднное поле Cсылка на офис партнера, в который отправлен запрос на одобрение ОН',
                    'description': '',
                    'data': {
                        "approvalPartnerOfficeId": 123456
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": 123456
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cсылка на офис партнера, в который отправлен запрос на одобрение ОН',
                    'description': '',
                    'data': {
                        "approvalPartnerOfficeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cсылка на офис партнера, в который отправлен запрос на одобрение ОН',
                    'description': '',
                    'data': {
                        "approvalPartnerOfficeId": 'String99'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": 'String99'
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cсылка на офис партнера, в который отправлен запрос на одобрение ОН',
                    'description': '',
                    'data': {
                        "approvalPartnerOfficeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": None
                        }]
                    }
                }
            ],
            "approveCounter": [
                {
                    'name': 'валиднное поле Cчетчик по дате одобрения',
                    'description': '',
                    'data': {
                        "approveCounter": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": 12345
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cчетчик по дате одобрения',
                    'description': '',
                    'data': {
                        "approveCounter": '12345'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": '12345'
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cчетчик по дате одобрения',
                    'description': '',
                    'data': {
                        "approveCounter": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Cчетчик по дате одобрения',
                    'description': '',
                    'data': {
                        "approveCounter": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": None
                        }]
                    }
                }
            ],
            "approvedSum": [
                {
                    'name': 'не валиднное поле Cчетчик по дате одобрения',
                    'description': '',
                    'data': {
                        "approvedSum": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Одобренная сумма кредита',
                    'description': '',
                    'data': {
                        "approvedSum": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Одобренная сумма кредита',
                    'description': '',
                    'data': {
                        "approvedSum": '12345'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": '12345'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле Одобренная сумма кредита',
                    'description': '',
                    'data': {
                        "approvedSum": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": 12345
                        }]
                    }
                },
                {
                    'name': ' валиднное поле Одобренная сумма кредита',
                    'description': '',
                    'data': {
                        "approvedSum": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": 12345.5
                        }]
                    }
                },
            ],
            "authorId": [
                {
                    'name': ' валидный уникальный идентификатор пользователя, создавшего сделку',
                    'description': '',
                    'data': {
                        "authorId": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": 12345
                        }]
                    }
                },
                {
                    'name': ' не валидный уникальный идентификатор пользователя, создавшего сделку',
                    'description': '',
                    'data': {
                        "authorId": 12345.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": 12345.6
                        }]
                    }
                },
                {
                    'name': ' не валидный уникальный идентификатор пользователя, создавшего сделку',
                    'description': '',
                    'data': {
                        "authorId": '12345.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": '12345.6'
                        }]
                    }
                },
                {
                    'name': ' не валидный уникальный идентификатор пользователя, создавшего сделку',
                    'description': '',
                    'data': {
                        "authorId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный уникальный идентификатор пользователя, создавшего сделку',
                    'description': '',
                    'data': {
                        "authorId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": None
                        }]
                    }
                }
            ],
            "availableObjectDocuments": [
                {
                    'name': ' валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": True
                        }]
                    }
                },
                {
                    'name': ' валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": 'True'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": 'True'
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": None
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": 1234
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": 1234
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": '1.2'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": '1.2'
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что в заявке на кредит есть еще документы по одобрению ОН',
                    'description': '',
                    'data': {
                        "availableObjectDocuments": [1, 1.2, 'string']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": [1, 1.2, 'string']
                        }]
                    }
                }
            ],
            "availableObjectDocumentsChangeDate": [
                {
                    'name': ' валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": '12.09.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": '12.09.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": '12.09.2017'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": '12.09.2017'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": True
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": True
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": 123
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": ''
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки соовтетствующего маркера',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": None
                        }]
                    }
                }
            ],
            "availableObjectDocumentsChangeUserId": [
                {
                    'name': ' валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": 123
                        }]
                    }
                },
                {
                    'name': ' не валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": ''
                        }]
                    }
                },
                {
                    'name': ' не валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": None
                        }]
                    }
                },
                {
                    'name': ' не валидная идентификатор пользователя, который выставил соответствующий маркер',
                    'description': '',
                    'data': {
                        "availableObjectDocumentsChangeUserId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": [123.6]
                        }]
                    }
                }
            ],
            "backwashPartnerOfficeId": [
                {
                    'name': ' валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": 123
                        }]
                    }
                },
                {
                    'name': ' не валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": '123.6'
                        }]
                    }
                },
                {
                    'name': ' не валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": ''
                        }]
                    }
                },
                {
                    'name': ' не валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": None
                        }]
                    }
                },
                {
                    'name': ' не валидная cсылка на офис партнера, в которы был направлен лид',
                    'description': '',
                    'data': {
                        "backwashPartnerOfficeId": ['123.6']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": ['123.6']
                        }]
                    }
                }
            ],
            "bankOfficeId": [
                {
                    'name': ' валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": '123'
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": ['123']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": ['123']
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": 123.5
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор цик, к которому относится заявка (только для импортированных)',
                    'description': '',
                    'data': {
                        "bankOfficeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": None
                        }]
                    }
                }
            ],
            "bankTbId": [
                {
                    'name': ' валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": 123
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": 123.5
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": '123.5'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": '123.5'
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": None
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор банка, к которому относится заявка',
                    'description': '',
                    'data': {
                        "bankTbId": [123]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": [123]
                        }]
                    }
                }
            ],
            "browserSignature": [
                {
                    'name': ' валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": 123
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": [123]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": [123]
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": 123.5
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, который показывает, с какого компьютера была создана сущность',
                    'description': '',
                    'data': {
                        "browserSignature": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": None
                        }]
                    }
                }
            ],
            "casAccessSend": [
                {
                    'name': ' валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": True
                        }]
                    }
                },
                {
                    'name': ' валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": False
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": 'True'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": 'True'
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": 123.5
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": [123.5]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": [123.5]
                        }]
                    }
                },
                {
                    'name': 'не валидный маркер, показывающий что клиент согласился воспользоваться ЛКЗ (надо для легаси данных)',
                    'description': '',
                    'data': {
                        "casAccessSend": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": None
                        }]
                    }
                }

            ],
            "casAccessSendDate": [
                {
                    'name': 'валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата создания ЛКЗ',
                    'description': '',
                    'data': {
                        "casAccessSendDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": ''
                        }]
                    }
                }

            ],
            "cellDocumentSigned": [
                {
                    'name': ' валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": True
                        }]
                    }
                },
                {
                    'name': ' валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": False
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": 123
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": [1]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": []
                        }]
                    }
                },
                {
                    'name': ' не валидный хеш, aренда ячейки',
                    'description': '',
                    'data': {
                        "cellDocumentSigned": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": None
                        }]
                    }
                }

            ],
            "cityId": [
                {
                    'name': 'валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": 123.5
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": '123.5'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": '123.5'
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": ['123.5']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": ['123.5']
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на город, в цик которого отправляется заявка на кредит',
                    'description': '',
                    'data': {
                        "cityId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": None
                        }]
                    }
                }
            ],
            "copyExists": [
                {
                    'name': 'валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": True
                        }]
                    }
                },
                {
                    'name': 'валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": False
                        }]
                    }
                },
                {
                    'name': 'не валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": '123'
                        }]
                    }
                },
                {
                    'name': 'не валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": ['123']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": ['123']
                        }]
                    }
                },
                {
                    'name': 'не валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная, есть ли копия',
                    'description': '',
                    'data': {
                        "copyExists": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": None
                        }]
                    }
                }
            ],
            "costFromEst": [
                {
                    'name': ' валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": 123
                        }]
                    }
                },
                {
                    'name': ' валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": 123.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": 123.5
                        }]
                    }
                },
                {
                    'name': ' валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": 0
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": 0
                        }]
                    }
                },
                {
                    'name': ' не валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": -123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": -123.5
                        }]
                    }
                },
                {
                    'name': ' не валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": ''
                        }]
                    }
                },
                {
                    'name': ' не валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": [1]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": [1]
                        }]
                    }
                },
                {
                    'name': ' не валидная стоимость из отчета об оценке',
                    'description': '',
                    'data': {
                        "costFromEst": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": None
                        }]
                    }
                }
            ],
            "creditAnalysisId": [
                {
                    'name': ' валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": 123
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": '123.6'
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": None
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": -123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": -123
                        }]
                    }
                },
                {
                    'name': ' не валидный идентификатор из словаря creditAnalysis',
                    'description': '',
                    'data': {
                        "creditAnalysisId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": 0
                        }]
                    }
                }
            ],
            "crmReasonComment": [
                {
                    'name': ' валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": '123'
                        }]
                    }
                },
                {
                    'name': ' не валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": 123
                        }]
                    }
                },
                {
                    'name': ' не валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": [123]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": [123]
                        }]
                    }
                },
                {
                    'name': ' не валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": 0
                        }]
                    }
                },
                {
                    'name': ' валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": ''
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": 123.5
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": 123.5
                        }]
                    }
                },
                {
                    'name': ' не валидный коммент',
                    'description': '',
                    'data': {
                        "crmReasonComment": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": None
                        }]
                    }
                }

            ],
            "draftCreateDate": [
                {
                    'name': ' валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": '12.09.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": '12.09.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": '12.09.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": '12.09.2019'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": ''
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": 123
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера черновика',
                    'description': '',
                    'data': {
                        "draftCreateDate": [123]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": [123]
                        }]
                    }
                }
            ],
            "draftDate": [
                {
                    'name': 'валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": '12.03.2016'
                        }]
                    }
                },
                {
                    'name': 'не валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": '12.03.2019'
                        }]
                    }
                },
                {
                    'name': 'не валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": None
                        }]
                    }
                },
                {
                    'name': 'не валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная дата снятия маркера черновика',
                    'description': '',
                    'data': {
                        "draftDate": ['12.03.2019']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": ['12.03.2019']
                        }]
                    }
                }
            ],
            "firstApprovedDate": [
                {
                    'name': 'валидная дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": '12.03.2016'
                        }]
                    }
                },
                {
                    'name': 'не дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": '12.03.2019'
                        }]
                    }
                },
                {
                    'name': 'не валидная дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": None
                        }]
                    }
                },
                {
                    'name': 'не валидная дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": 123
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная дата первого одобрения сделки',
                    'description': '',
                    'data': {
                        "firstApprovedDate": ['12.03.2019']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": ['12.03.2019']
                        }]
                    }
                }
            ],
            "id": [
                {
                    'name': 'валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": None
                        }]
                    }
                },
                {
                    'name': 'не валидный id чего именно id- не указано',
                    'description': '',
                    'data': {
                        "id": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": -1
                        }]
                    }
                }
            ],
            "imikParameters": [
                {
                    'name': 'валидный текст, содержащий все параметры кредитного калькулятора',
                    'description': '',
                    'data': {
                        "imikParameters": '123y'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": '123y'
                        }]
                    }
                },
                {
                    'name': 'не валидный текст, содержащий все параметры кредитного калькулятора',
                    'description': '',
                    'data': {
                        "imikParameters": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный текст, содержащий все параметры кредитного калькулятора',
                    'description': '',
                    'data': {
                        "imikParameters": ['']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": ['']
                        }]
                    }
                },
                {
                    'name': 'не валидный текст, содержащий все параметры кредитного калькулятора',
                    'description': '',
                    'data': {
                        "imikParameters": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": None
                        }]
                    }
                }
            ],
            "importedUserId": [
                {
                    'name': 'валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": '123'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": '123'
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": -1
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": [-1]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": [-1]
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор пользователя, который импортировал сделку',
                    'description': '',
                    'data': {
                        "importedUserId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": 0
                        }]
                    }
                }
            ],
            "initialFee": [
                {
                    'name': 'валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": 80
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": 80
                        }]
                    }
                },
                {
                    'name': 'валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": 80.6
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": 80.6
                        }]
                    }
                },
                {
                    'name': 'валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": 0
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": -80
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": -80
                        }]
                    }
                },
                {
                    'name': 'не валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": [-80]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": [-80]
                        }]
                    }
                },
                {
                    'name': 'не валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": '-80'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": '-80'
                        }]
                    }
                },
                {
                    'name': 'не валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный ?первоначальная комиссия',
                    'description': '',
                    'data': {
                        "initialFee": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": None
                        }]
                    }
                }

            ],
            "insuranceDocumentSigned": [
                {
                    'name': 'валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": False
                        }]
                    }
                },
                {
                    'name': 'валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": True
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": '12'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": '12'
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": -9
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": -9
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": 9
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": 9
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": ['12']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": ['12']
                        }]
                    }
                },
                {
                    'name': 'не валидный- страховка подписана',
                    'description': '',
                    'data': {
                        "insuranceDocumentSigned": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": None
                        }]
                    }
                }
            ],
            "interestRate": [
                {
                    'name': 'валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": 101
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": 101
                        }]
                    }
                },
                {
                    'name': 'валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": 101.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": 101.5
                        }]
                    }
                },
                {
                    'name': 'не валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": '101'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": '101'
                        }]
                    }
                },

                {
                    'name': 'не валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": '101%'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": '101%'
                        }]
                    }
                },
                {
                    'name': 'не валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": ['101%']
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": ['101%']
                        }]
                    }
                },
                {
                    'name': 'не валидная % ставка',
                    'description': '',
                    'data': {
                        "interestRate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": None
                        }]
                    }
                }

            ],
            "isDraft": [
                {
                    'name': 'валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": True
                        }]
                    }
                },
                {
                    'name': 'валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер черновика',
                    'description': '',
                    'data': {
                        "isDraft": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": None
                        }]
                    }
                }
            ],
            "wasDraft": [
                {
                    'name': 'валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": True
                        }]
                    }
                },
                {
                    'name': 'валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер о том, что заявка была черновиком',
                    'description': '',
                    'data': {
                        "wasDraft": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": None
                        }]
                    }
                }
            ],
            "isImported": [
                {
                    'name': ' валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, была ли эта сделка импортирована из внешниз систем',
                    'description': '',
                    'data': {
                        "isImported": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": None
                        }]
                    }
                }
            ],
            "isMorton": [
                {
                    'name': ' валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что сделка получена от Мортона',
                    'description': '',
                    'data': {
                        "isMorton": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": None
                        }]
                    }
                }
            ],
            "isPortalLogin": [
                {
                    'name': ' валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер есть ли логин в портале',
                    'description': '',
                    'data': {
                        "isPortalLogin": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": None
                        }]
                    }
                }
            ],
            "isTraining": [
                {
                    'name': ' валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер учебной сделки',
                    'description': '',
                    'data': {
                        "isTraining": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isTraining": None
                        }]
                    }
                }
            ],
            "isUrm": [
                {
                    'name': ' валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявку подал пользователь с ролью УРМ',
                    'description': '',
                    'data': {
                        "isUrm": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": None
                        }]
                    }
                }
            ],
            "plannedBorrow": [
                {
                    'name': ' валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, показывающий что заемщик хочет взять денег, а не просто прошел одобрение чтобы проверить свою кредитную историю',
                    'description': '',
                    'data': {
                        "plannedBorrow": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": None
                        }]
                    }
                }
            ],
            "propertyApproval": [
                {
                    'name': ' валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того что в составе заявки на кредит есть и документы заявки на одобрение ОН',
                    'description': '',
                    'data': {
                        "propertyApproval": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": None
                        }]
                    }
                }
            ],
            "recovered": [
                {
                    'name': ' валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер, который показывает, что сделка просрочила свои 60 дней, но была все равно \"восстановлена\" поскольку заемщик на сделку вышел в короткое время',
                    'description': '',
                    'data': {
                        "recovered": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": None
                        }]
                    }
                }
            ],
            "urmCik": [
                {
                    'name': ' валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": False
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": 101
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка подана УРМом, оторый сидит в ЦИК',
                    'description': '',
                    'data': {
                        "urmCik": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": None
                        }]
                    }
                }
            ],
            "viewOnlyForOwner": [
                {
                    'name': ' валидный маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": True
                        }]
                    }
                },

                {
                    'name': 'валидный маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": False
                        }]
                    }
                },
                {
                    'name': ' не маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": 101
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": 101
                        }]
                    }
                },
                {
                    'name': ' не маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": 101.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": 101.6
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": [101]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": [101]
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": ''
                        }]
                    }
                },
                {
                    'name': ' не валидный маркер того, что заявка видна только автору',
                    'description': '',
                    'data': {
                        "viewOnlyForOwner": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": None
                        }]
                    }
                }
            ],
            "issuedSum": [
                {
                    'name': 'не валиднное поле Выданный кредит',
                    'description': '',
                    'data': {
                        "issuedSum": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле  Выданный кредит',
                    'description': '',
                    'data': {
                        "issuedSum": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле  Выданный кредит',
                    'description': '',
                    'data': {
                        "approvedSum": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле  Выданный кредит',
                    'description': '',
                    'data': {
                        "issuedSum": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": 12345
                        }]
                    }
                },
                {
                    'name': ' валиднное поле  Выданный кредит',
                    'description': '',
                    'data': {
                        "issuedSum": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": 12345.5
                        }]
                    }
                }
            ],
            "monthlyPayment": [
                {
                    'name': 'не валиднное поле ?? Ежемесячный платеж',
                    'description': '',
                    'data': {
                        "monthlyPayment": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле ?? Ежемесячный платеж',
                    'description': '',
                    'data': {
                        "monthlyPayment": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле ?? Ежемесячный платеж',
                    'description': '',
                    'data': {
                        "monthlyPayment": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле ?? Ежемесячный платеж',
                    'description': '',
                    'data': {
                        "monthlyPayment": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": 12345
                        }]
                    }
                },
                {
                    'name': ' валиднное поле ?? Ежемесячный платеж',
                    'description': '',
                    'data': {
                        "monthlyPayment": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": 12345.5
                        }]
                    }
                }
            ],
            "neededRevenue": [
                {
                    'name': 'не валиднное поле neededRevenue',
                    'description': '',
                    'data': {
                        "neededRevenue": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле neededRevenue',
                    'description': '',
                    'data': {
                        "neededRevenue": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле neededRevenue',
                    'description': '',
                    'data': {
                        "neededRevenue": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле neededRevenue',
                    'description': '',
                    'data': {
                        "neededRevenue": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": 12345
                        }]
                    }
                },
                {
                    'name': 'валиднное поле neededRevenue',
                    'description': '',
                    'data': {
                        "neededRevenue": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": 12345.5
                        }]
                    }
                }
            ],
            "objectLivingSpace": [
                {
                    'name': 'не валиднное поле Жилая площадь объекта',
                    'description': '',
                    'data': {
                        "objectLivingSpace": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Жилая площадь объекта',
                    'description': '',
                    'data': {
                        "objectLivingSpace": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле  Жилая площадь объекта',
                    'description': '',
                    'data': {
                        "objectLivingSpace": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле  Жилая площадь объекта',
                    'description': '',
                    'data': {
                        "objectLivingSpace": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": 12345
                        }]
                    }
                },
                {
                    'name': 'валиднное поле  Жилая площадь объекта',
                    'description': '',
                    'data': {
                        "objectLivingSpace": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": 12345.5
                        }]
                    }
                }
            ],
            "objectSpace": [
                {
                    'name': 'не валиднное поле Площадь объекта',
                    'description': '',
                    'data': {
                        "objectSpace": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Площадь объекта',
                    'description': '',
                    'data': {
                        "objectSpace": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле  Площадь объекта',
                    'description': '',
                    'data': {
                        "objectSpace": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле  Площадь объекта',
                    'description': '',
                    'data': {
                        "objectSpace": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": 12345
                        }]
                    }
                },
                {
                    'name': 'валиднное поле  Площадь объекта',
                    'description': '',
                    'data': {
                        "objectSpace": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": 12345.5
                        }]
                    }
                }
            ],
            "requestedSum": [
                {
                    'name': 'не валиднное поле Запрошенная сумма кредита',
                    'description': '',
                    'data': {
                        "requestedSum": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": None
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Запрошенная сумма кредита',
                    'description': '',
                    'data': {
                        "requestedSum": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": ''
                        }]
                    }
                },
                {
                    'name': 'не валиднное поле Запрошенная сумма кредита',
                    'description': '',
                    'data': {
                        "requestedSum": 'issuedSum'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": 'issuedSum'
                        }]
                    }
                },
                {
                    'name': 'валиднное поле Запрошенная сумма кредита',
                    'description': '',
                    'data': {
                        "requestedSum": 12345
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": 12345
                        }]
                    }
                },
                {
                    'name': 'валиднное поле Запрошенная сумма кредита',
                    'description': '',
                    'data': {
                        "requestedSum": 12345.5
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": 12345.5
                        }]
                    }
                }
            ],
            "issuedCounter": [
                {
                    'name': 'валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": None
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате выдачи',
                    'description': '',
                    'data': {
                        "issuedCounter": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": -1
                        }]
                    }
                }
            ],
            "loanPeriod": [
                {
                    'name': 'валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": None
                        }]
                    }
                },
                {
                    'name': 'не валидный срок кредита',
                    'description': '',
                    'data': {
                        "loanPeriod": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": -1
                        }]
                    }
                }
            ],
            "mainDocument": [
                {
                    'name': 'валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": None
                        }]
                    }
                },
                {
                    'name': 'не валидный договор купли продажи(сейчас не используется)',
                    'description': '',
                    'data': {
                        "mainDocument": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": -1
                        }]
                    }
                }
            ],
            "mikId": [
                {
                    'name': 'валидный уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный  уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный  уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный  уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный  уникальный идентификатор ответственного за сделку МИКа',
                    'description': '',
                    'data': {
                        "mikId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": -1
                        }]
                    }
                }
            ],
            "mrpOfApproval": [
                {
                    'name': 'валидный валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": 0
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": None
                        }]
                    }
                },
                {
                    'name': 'не валидная cсылка на МРП, который отвечал за офис партнера, подавшего заявку на момент одобрения заявки',
                    'description': '',
                    'data': {
                        "mrpOfApproval": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": -1
                        }]
                    }
                }
            ],
            "objectContractCost": [
                {
                    'name': 'валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 0
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": None
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": -1
                        }]
                    }
                }
            ],
            "objectTypeId": [
                {
                    'name': 'валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 0
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": None
                        }]
                    }
                },
                {
                    'name': 'не валидная стоимость объекта по договору',
                    'description': '',
                    'data': {
                        "objectContractCost": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": -1
                        }]
                    }
                }
            ],
            "officeBranchId": [
                {
                    'name': 'валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный номер ЦИК в структуре банка',
                    'description': '',
                    'data': {
                        "officeBranchId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeBranchId": -1
                        }]
                    }
                }
            ],
            "officeId": [
                {
                    'name': 'валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор ЦИК, выбранного при создании заявки на кредит',
                    'description': '',
                    'data': {
                        "officeId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "officeId": -1
                        }]
                    }
                }
            ],
            "partnerOfficeId": [
                {
                    'name': 'валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный уникальный идентификатор офиса партнера, от лица которого может быть подана заявка',
                    'description': '',
                    'data': {
                        "partnerOfficeId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "partnerOfficeId": -1
                        }]
                    }
                }
            ],
            "productTypeId": [
                {
                    'name': 'валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря продуктов',
                    'description': '',
                    'data': {
                        "productTypeId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "productTypeId": -1
                        }]
                    }
                }
            ],
            "sendCounter": [
                {
                    'name': 'валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": None
                        }]
                    }
                },
                {
                    'name': 'не валидный счетчик по дате подачи ',
                    'description': '',
                    'data': {
                        "sendCounter": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": -1
                        }]
                    }
                }
            ],
            "subproductTypeId": [
                {
                    'name': 'валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный идентификатор из словаря субпродуктов',
                    'description': '',
                    'data': {
                        "subproductTypeId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": -1
                        }]
                    }
                }
            ],
            "sumSupposes": [
                {
                    'name': 'валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": 123
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": 0
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": ''
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": None
                        }]
                    }
                },
                {
                    'name': 'не валидная предполодительная сумма объекта',
                    'description': '',
                    'data': {
                        "sumSupposes": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": -1
                        }]
                    }
                }
            ],
            "transactId": [
                {
                    'name': 'валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": 123
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": 123
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": 123.6
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": 0
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": 0
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": [123.6]
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": '123.6'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": '123.6'
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": ''
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": None
                        }]
                    }
                },
                {
                    'name': 'не валидный номер транзакт',
                    'description': '',
                    'data': {
                        "transactId": -1
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": -1
                        }]
                    }
                }
            ],
            "lastApprovedDate": [
                {
                    'name': 'валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последнего одобрения сделки',
                    'description': '',
                    'data': {
                        "lastApprovedDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastApprovedDate": ''
                        }]
                    }
                }
            ],
            "lastIssueDate": [
                {
                    'name': 'валидная дата дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата последней выдачи сделки',
                    'description': '',
                    'data': {
                        "lastIssueDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastIssueDate": ''
                        }]
                    }
                }
            ],
            "lastRejectedDate": [
                {
                    'name': 'валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата отмены сделки',
                    'description': '',
                    'data': {
                        "lastRejectedDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "lastRejectedDate": ''
                        }]
                    }
                }
            ],
            "nextContactDate": [
                {
                    'name': 'валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "nextContactDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "nextContactDate": ''
                        }]
                    }
                }
            ],
            "plannedIssueDate": [
                {
                    'name': 'валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная cледующая дата контакта',
                    'description': '',
                    'data': {
                        "plannedIssueDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedIssueDate": ''
                        }]
                    }
                }
            ],
            "recoverDate": [
                {
                    'name': 'валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата восстановления',
                    'description': '',
                    'data': {
                        "recoverDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "recoverDate": ''
                        }]
                    }
                }
            ],
            "trainingDate": [
                {
                    'name': 'валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": '123'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": '123'
                        }]
                    }
                },
                {
                    'name': ' валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": '12.03.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": '12.3.2016'
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": '12.03.2019'
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": '12.3.2019'
                        }]
                    }
                },

                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": 123.6
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": 123.6
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": [123.6]
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": [123.6]
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": None
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": None
                        }]
                    }
                },
                {
                    'name': ' не валидная дата установки маркера учебной сделки',
                    'description': '',
                    'data': {
                        "trainingDate": ''
                    },
                    'expected': {
                        "success": False,
                        "data": [{
                            "dealStatusId": 8060,
                            "trainingDate": ''
                        }]
                    }
                }
            ],
        },
    'deal_fields_put_validation':
        {"dealId": [
            {
                'name': 'Обновление сделки с null до валидного ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": None
                },
                'data': {
                    "dealId": 12020
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "dealId": 12020
                    }]
                }
            },
            {
                'name': 'Обновление сделки с валидного ID из словаря до null для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": 11
                },
                'data': {
                    "dealId": None
                },
                'expected': {
                    "success": True,
                    "data": [{
                        "dealStatusId": 8060,
                        "dealId": None
                    }]
                }
            },
            {
                'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": 11
                },
                'data': {
                    "dealId": 11111111
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
                'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": 11
                },
                'data': {
                    "dealId": 12.010
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
                'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": 11
                },
                'data': {
                    "dealId": "12010"
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
                'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": None
                },
                'data': {
                    "dealId": 12.010
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
                'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": None
                },
                'data': {
                    "dealId": 11111111
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
                'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля dealId',
                'description': '',
                'precondition': {
                    "dealId": None
                },
                'data': {
                    "dealId": "12010"
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
            "casId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": None
                    },
                    'data': {
                        "casId": 120200
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": 120200
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": 11
                    },
                    'data': {
                        "casId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": 11
                    },
                    'data': {
                        "casId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": 11
                    },
                    'data': {
                        "casId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": 11
                    },
                    'data': {
                        "casId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": None
                    },
                    'data': {
                        "casId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": None
                    },
                    'data': {
                        "casId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля casId',
                    'description': '',
                    'precondition': {
                        "casId": None
                    },
                    'data': {
                        "casId": "12010"
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
                }
            ],
            "agreementDocument": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": None
                    },
                    'data': {
                        "agreementDocument": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": 1
                    },
                    'data': {
                        "agreementDocument": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "agreementDocument": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": 1
                    },
                    'data': {
                        "agreementDocument": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": 1
                    },
                    'data': {
                        "agreementDocument": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": 11
                    },
                    'data': {
                        "agreementDocument": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": None
                    },
                    'data': {
                        "agreementDocument": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": None
                    },
                    'data': {
                        "agreementDocument": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля agreementDocument',
                    'description': '',
                    'precondition': {
                        "agreementDocument": None
                    },
                    'data': {
                        "agreementDocument": "12010"
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
                }
            ],
            "approvalPartnerOfficeId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": None
                    },
                    'data': {
                        "approvalPartnerOfficeId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": 1
                    },
                    'data': {
                        "approvalPartnerOfficeId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvalPartnerOfficeId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": 1
                    },
                    'data': {
                        "approvalPartnerOfficeId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": 1
                    },
                    'data': {
                        "approvalPartnerOfficeId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": 11
                    },
                    'data': {
                        "approvalPartnerOfficeId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": None
                    },
                    'data': {
                        "approvalPartnerOfficeId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": None
                    },
                    'data': {
                        "approvalPartnerOfficeId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля approvalPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "approvalPartnerOfficeId": None
                    },
                    'data': {
                        "approvalPartnerOfficeId": "12010"
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
                }
            ],
            "approveCounter": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": None
                    },
                    'data': {
                        "approveCounter": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": 12020
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": 1
                    },
                    'data': {
                        "approveCounter": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approveCounter": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": 1
                    },
                    'data': {
                        "approveCounter": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": 1
                    },
                    'data': {
                        "approveCounter": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": 11
                    },
                    'data': {
                        "approveCounter": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": None
                    },
                    'data': {
                        "approveCounter": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": None
                    },
                    'data': {
                        "approveCounter": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля approveCounter',
                    'description': '',
                    'precondition': {
                        "approveCounter": None
                    },
                    'data': {
                        "approveCounter": "12010"
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
                }
            ],
            "authorId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": None
                    },
                    'data': {
                        "authorId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": 12020
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": 1
                    },
                    'data': {
                        "authorId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "authorId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": 1
                    },
                    'data': {
                        "authorId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": 1
                    },
                    'data': {
                        "authorId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": 11
                    },
                    'data': {
                        "authorId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": None
                    },
                    'data': {
                        "authorId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": None
                    },
                    'data': {
                        "authorId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля authorId',
                    'description': '',
                    'precondition': {
                        "authorId": None
                    },
                    'data': {
                        "authorId": "12010"
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
                }
            ],
            "availableObjectDocumentsChangeUserId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": 12020
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": 1
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeUserId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": 1
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": 1
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": 11
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля availableObjectDocumentsChangeUserId',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeUserId": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeUserId": "12010"
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
                }
            ],
            "backwashPartnerOfficeId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": None
                    },
                    'data': {
                        "backwashPartnerOfficeId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": 1
                    },
                    'data': {
                        "backwashPartnerOfficeId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": 1
                    },
                    'data': {
                        "backwashPartnerOfficeId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": 1
                    },
                    'data': {
                        "backwashPartnerOfficeId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": 11
                    },
                    'data': {
                        "backwashPartnerOfficeId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": None
                    },
                    'data': {
                        "backwashPartnerOfficeId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": None
                    },
                    'data': {
                        "backwashPartnerOfficeId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля backwashPartnerOfficeId',
                    'description': '',
                    'precondition': {
                        "backwashPartnerOfficeId": None
                    },
                    'data': {
                        "backwashPartnerOfficeId": "12010"
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
                }
            ],
            "bankOfficeId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": None
                    },
                    'data': {
                        "bankOfficeId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankOfficeId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": 1
                    },
                    'data': {
                        "bankOfficeId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "backwashPartnerOfficeId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": 1
                    },
                    'data': {
                        "bankOfficeId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": 1
                    },
                    'data': {
                        "bankOfficeId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": 11
                    },
                    'data': {
                        "bankOfficeId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": None
                    },
                    'data': {
                        "bankOfficeId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": None
                    },
                    'data': {
                        "bankOfficeId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": None
                    },
                    'data': {
                        "bankOfficeId": "12010"
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
                }
            ],
            "bankTbId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": None
                    },
                    'data': {
                        "bankTbId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": 1
                    },
                    'data': {
                        "bankTbId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "bankTbId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля bankOfficeId',
                    'description': '',
                    'precondition': {
                        "bankTbId": 1
                    },
                    'data': {
                        "bankTbId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": 1
                    },
                    'data': {
                        "bankTbId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": 11
                    },
                    'data': {
                        "bankTbId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": None
                    },
                    'data': {
                        "bankTbId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankTbId": None
                    },
                    'data': {
                        "bankTbId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля bankTbId',
                    'description': '',
                    'precondition': {
                        "bankOfficeId": None
                    },
                    'data': {
                        "bankOfficeId": "12010"
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
                }
            ],
            "cityId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": None
                    },
                    'data': {
                        "cityId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": 1
                    },
                    'data': {
                        "cityId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cityId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": 1
                    },
                    'data': {
                        "cityId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": 1
                    },
                    'data': {
                        "cityId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": 11
                    },
                    'data': {
                        "cityId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": None
                    },
                    'data': {
                        "cityId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": None
                    },
                    'data': {
                        "cityId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля cityId',
                    'description': '',
                    'precondition': {
                        "cityId": None
                    },
                    'data': {
                        "cityId": "12010"
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
                }
            ],
            "creditAnalysisId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": None
                    },
                    'data': {
                        "creditAnalysisId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": 1
                    },
                    'data': {
                        "creditAnalysisId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "creditAnalysisId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": 1
                    },
                    'data': {
                        "creditAnalysisId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": 1
                    },
                    'data': {
                        "creditAnalysisId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": 11
                    },
                    'data': {
                        "creditAnalysisId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": None
                    },
                    'data': {
                        "creditAnalysisId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": None
                    },
                    'data': {
                        "creditAnalysisId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля creditAnalysisId',
                    'description': '',
                    'precondition': {
                        "creditAnalysisId": None
                    },
                    'data': {
                        "creditAnalysisId": "12010"
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
                }
            ],
            "id": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": None
                    },
                    'data': {
                        "id": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля id',
                    'description': '',
                    'precondition': {
                        "id": 1
                    },
                    'data': {
                        "id": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "id": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": 1
                    },
                    'data': {
                        "id": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": 1
                    },
                    'data': {
                        "id": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": 11
                    },
                    'data': {
                        "id": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": None
                    },
                    'data': {
                        "id": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": None
                    },
                    'data': {
                        "id": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля id',
                    'description': '',
                    'precondition': {
                        "id": None
                    },
                    'data': {
                        "id": "12010"
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
                }
            ],
            "importedUserId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": None
                    },
                    'data': {
                        "importedUserId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": 1
                    },
                    'data': {
                        "importedUserId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "importedUserId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": 1
                    },
                    'data': {
                        "importedUserId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": 1
                    },
                    'data': {
                        "importedUserId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": 11
                    },
                    'data': {
                        "importedUserId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": None
                    },
                    'data': {
                        "importedUserId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": None
                    },
                    'data': {
                        "importedUserId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля importedUserId',
                    'description': '',
                    'precondition': {
                        "importedUserId": None
                    },
                    'data': {
                        "importedUserId": "12010"
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
                }
            ],
            "issuedCounter": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": None
                    },
                    'data': {
                        "issuedCounter": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "importedUserId": 1
                    },
                    'data': {
                        "issuedCounter": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedCounter": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": 1
                    },
                    'data': {
                        "issuedCounter": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": 1
                    },
                    'data': {
                        "issuedCounter": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": 11
                    },
                    'data': {
                        "issuedCounter": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": None
                    },
                    'data': {
                        "issuedCounter": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": None
                    },
                    'data': {
                        "issuedCounter": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля issuedCounter',
                    'description': '',
                    'precondition': {
                        "issuedCounter": None
                    },
                    'data': {
                        "issuedCounter": "12010"
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
                }
            ],
            "loanPeriod": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": None
                    },
                    'data': {
                        "loanPeriod": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": 1
                    },
                    'data': {
                        "loanPeriod": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "loanPeriod": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": 1
                    },
                    'data': {
                        "loanPeriod": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": 1
                    },
                    'data': {
                        "loanPeriod": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": 11
                    },
                    'data': {
                        "loanPeriod": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": None
                    },
                    'data': {
                        "loanPeriod": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": None
                    },
                    'data': {
                        "loanPeriod": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля loanPeriod',
                    'description': '',
                    'precondition': {
                        "loanPeriod": None
                    },
                    'data': {
                        "loanPeriod": "12010"
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
                }
            ],
            "mainDocument": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": None
                    },
                    'data': {
                        "mainDocument": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": 1
                    },
                    'data': {
                        "mainDocument": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mainDocument": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": 1
                    },
                    'data': {
                        "mainDocument": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": 1
                    },
                    'data': {
                        "mainDocument": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": 11
                    },
                    'data': {
                        "mainDocument": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": None
                    },
                    'data': {
                        "mainDocument": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": None
                    },
                    'data': {
                        "mainDocument": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля mainDocument',
                    'description': '',
                    'precondition': {
                        "mainDocument": None
                    },
                    'data': {
                        "mainDocument": "12010"
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
                }
            ],
            "mikId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": None
                    },
                    'data': {
                        "mikId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": 1
                    },
                    'data': {
                        "mikId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mikId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": 1
                    },
                    'data': {
                        "mikId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": 1
                    },
                    'data': {
                        "mikId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": 11
                    },
                    'data': {
                        "mikId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": None
                    },
                    'data': {
                        "mikId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": None
                    },
                    'data': {
                        "mikId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля mikId',
                    'description': '',
                    'precondition': {
                        "mikId": None
                    },
                    'data': {
                        "mikId": "12010"
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
                }
            ],
            "mrpOfApproval": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": None
                    },
                    'data': {
                        "mrpOfApproval": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": 1
                    },
                    'data': {
                        "mrpOfApproval": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "mrpOfApproval": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": 1
                    },
                    'data': {
                        "mrpOfApproval": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": 1
                    },
                    'data': {
                        "mrpOfApproval": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": 11
                    },
                    'data': {
                        "mrpOfApproval": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": None
                    },
                    'data': {
                        "mrpOfApproval": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": None
                    },
                    'data': {
                        "mrpOfApproval": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля mrpOfApproval',
                    'description': '',
                    'precondition': {
                        "mrpOfApproval": None
                    },
                    'data': {
                        "mrpOfApproval": "12010"
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
                }
            ],
            "objectContractCost": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": None
                    },
                    'data': {
                        "objectContractCost": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": 1
                    },
                    'data': {
                        "objectContractCost": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectContractCost": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": 1
                    },
                    'data': {
                        "objectContractCost": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": 1
                    },
                    'data': {
                        "objectContractCost": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": 11
                    },
                    'data': {
                        "objectContractCost": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": None
                    },
                    'data': {
                        "objectContractCost": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": None
                    },
                    'data': {
                        "objectContractCost": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля objectContractCost',
                    'description': '',
                    'precondition': {
                        "objectContractCost": None
                    },
                    'data': {
                        "objectContractCost": "12010"
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
                }
            ],
            "objectTypeId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": None
                    },
                    'data': {
                        "objectTypeId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectTypeId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": 1
                    },
                    'data': {
                        "objectTypeId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectTypeId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": 1
                    },
                    'data': {
                        "objectTypeId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": 1
                    },
                    'data': {
                        "objectTypeId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": 11
                    },
                    'data': {
                        "objectTypeId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": None
                    },
                    'data': {
                        "objectTypeId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": None
                    },
                    'data': {
                        "objectTypeId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля objectTypeId',
                    'description': '',
                    'precondition': {
                        "objectTypeId": None
                    },
                    'data': {
                        "objectTypeId": "12010"
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
                }
            ],
            "sendCounter": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": None
                    },
                    'data': {
                        "sendCounter": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": 1
                    },
                    'data': {
                        "sendCounter": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sendCounter": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": 1
                    },
                    'data': {
                        "sendCounter": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": 1
                    },
                    'data': {
                        "sendCounter": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": 11
                    },
                    'data': {
                        "sendCounter": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": None
                    },
                    'data': {
                        "sendCounter": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": None
                    },
                    'data': {
                        "sendCounter": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля sendCounter',
                    'description': '',
                    'precondition': {
                        "sendCounter": None
                    },
                    'data': {
                        "sendCounter": "12010"
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
                }
            ],
            "subproductTypeId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": None
                    },
                    'data': {
                        "subproductTypeId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "subproductTypeId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": 1
                    },
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
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": 1
                    },
                    'data': {
                        "subproductTypeId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": 1
                    },
                    'data': {
                        "subproductTypeId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": 11
                    },
                    'data': {
                        "subproductTypeId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": None
                    },
                    'data': {
                        "subproductTypeId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": None
                    },
                    'data': {
                        "subproductTypeId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля subproductTypeId',
                    'description': '',
                    'precondition': {
                        "subproductTypeId": None
                    },
                    'data': {
                        "subproductTypeId": "12010"
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
                }
            ],
            "sumSupposes": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": None
                    },
                    'data': {
                        "sumSupposes": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": 1
                    },
                    'data': {
                        "sumSupposes": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "sumSupposes": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": 1
                    },
                    'data': {
                        "sumSupposes": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": 1
                    },
                    'data': {
                        "sumSupposes": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": 11
                    },
                    'data': {
                        "sumSupposes": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": None
                    },
                    'data': {
                        "sumSupposes": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": None
                    },
                    'data': {
                        "sumSupposes": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля sumSupposes',
                    'description': '',
                    'precondition': {
                        "sumSupposes": None
                    },
                    'data': {
                        "sumSupposes": "12010"
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
                }
            ],
            "transactId": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": None
                    },
                    'data': {
                        "transactId": 1
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": 1
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": 1
                    },
                    'data': {
                        "transactId": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": 1
                    },
                    'data': {
                        "transactId": 11111111
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": 1
                    },
                    'data': {
                        "transactId": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до строкового ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": 11
                    },
                    'data': {
                        "transactId": "12010"
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": None
                    },
                    'data': {
                        "transactId": 12.010
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
                    'name': 'Обновление сделки с null из словаря до несуществующего ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": None
                    },
                    'data': {
                        "transactId": 11111111
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
                    'name': 'Обновление сделки с null из словаря до строкового ID из словаря для поля transactId',
                    'description': '',
                    'precondition': {
                        "transactId": None
                    },
                    'data': {
                        "transactId": "12010"
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
                }
            ],
            "createdTime": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "transactId": None
                    },
                    'data': {
                        "transactId": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "transactId": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": '12.08.2016'
                    },
                    'data': {
                        "createdTime": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "createdTime": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": '12.08.2016'
                    },
                    'data': {
                        "createdTime": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": '12.08.2016'
                    },
                    'data': {
                        "createdTime": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": '12.08.2016'
                    },
                    'data': {
                        "createdTime": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": None
                    },
                    'data': {
                        "createdTime": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля createdTime',
                    'description': '',
                    'precondition': {
                        "createdTime": None
                    },
                    'data': {
                        "createdTime": ''
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
            "modifiedTime": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": None
                    },
                    'data': {
                        "modifiedTime": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "modifiedTime": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": '12.08.2016'
                    },
                    'data': {
                        "modifiedTime": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "modifiedTime": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": '12.08.2016'
                    },
                    'data': {
                        "modifiedTime": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": '12.08.2016'
                    },
                    'data': {
                        "modifiedTime": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": '12.08.2016'
                    },
                    'data': {
                        "modifiedTime": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": None
                    },
                    'data': {
                        "modifiedTime": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля modifiedTime',
                    'description': '',
                    'precondition': {
                        "modifiedTime": None
                    },
                    'data': {
                        "modifiedTime": ''
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
            "availableObjectDocumentsChangeDate": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": '12.08.2016'
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocumentsChangeDate": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": '12.08.2016'
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": '12.08.2016'
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": '12.08.2016'
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля availableObjectDocumentsChangeDate',
                    'description': '',
                    'precondition': {
                        "availableObjectDocumentsChangeDate": None
                    },
                    'data': {
                        "availableObjectDocumentsChangeDate": ''
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
            "casAccessSendDate": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": None
                    },
                    'data': {
                        "casAccessSendDate": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": '12.08.2016'
                    },
                    'data': {
                        "casAccessSendDate": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSendDate": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": '12.08.2016'
                    },
                    'data': {
                        "casAccessSendDate": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": '12.08.2016'
                    },
                    'data': {
                        "casAccessSendDate": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": '12.08.2016'
                    },
                    'data': {
                        "casAccessSendDate": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": None
                    },
                    'data': {
                        "casAccessSendDate": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля casAccessSendDate',
                    'description': '',
                    'precondition': {
                        "casAccessSendDate": None
                    },
                    'data': {
                        "casAccessSendDate": ''
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
            "draftCreateDate": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": None
                    },
                    'data': {
                        "draftCreateDate": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": '12.08.2016'
                    },
                    'data': {
                        "draftCreateDate": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftCreateDate": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": '12.08.2016'
                    },
                    'data': {
                        "draftCreateDate": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": '12.08.2016'
                    },
                    'data': {
                        "draftCreateDate": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": '12.08.2016'
                    },
                    'data': {
                        "draftCreateDate": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": None
                    },
                    'data': {
                        "draftCreateDate": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля draftCreateDate',
                    'description': '',
                    'precondition': {
                        "draftCreateDate": None
                    },
                    'data': {
                        "casAccessSendDate": ''
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
            "draftDate": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": None
                    },
                    'data': {
                        "draftDate": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": '12.08.2016'
                    },
                    'data': {
                        "draftDate": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "draftDate": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": '12.08.2016'
                    },
                    'data': {
                        "draftDate": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": '12.08.2016'
                    },
                    'data': {
                        "draftDate": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": '12.08.2016'
                    },
                    'data': {
                        "draftDate": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": None
                    },
                    'data': {
                        "draftDate": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля draftDate',
                    'description': '',
                    'precondition': {
                        "draftDate": None
                    },
                    'data': {
                        "draftDate": ''
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
            "firstApprovedDate": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": None
                    },
                    'data': {
                        "firstApprovedDate": '12.08.2016'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": '12.08.2016'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": '12.08.2016'
                    },
                    'data': {
                        "firstApprovedDate": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "firstApprovedDate": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": '12.08.2016'
                    },
                    'data': {
                        "firstApprovedDate": '12.08.2019'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": '12.08.2016'
                    },
                    'data': {
                        "firstApprovedDate": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": '12.08.2016'
                    },
                    'data': {
                        "firstApprovedDate": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": None
                    },
                    'data': {
                        "firstApprovedDate": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля firstApprovedDate',
                    'description': '',
                    'precondition': {
                        "firstApprovedDate": None
                    },
                    'data': {
                        "firstApprovedDate": ''
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
            "imikParameters": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": None
                    },
                    'data': {
                        "imikParameters": '123gf'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": '123gf'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": '123gf'
                    },
                    'data': {
                        "imikParameters": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "imikParameters": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": '123gf'
                    },
                    'data': {
                        "imikParameters": '123gf'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": '123gf'
                    },
                    'data': {
                        "imikParameters": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": '12.08.2016'
                    },
                    'data': {
                        "imikParameters": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": None
                    },
                    'data': {
                        "imikParameters": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля imikParameters',
                    'description': '',
                    'precondition': {
                        "imikParameters": None
                    },
                    'data': {
                        "imikParameters": ''
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
            "crmReasonComment": [
                {
                    'name': 'Обновление сделки с null до валидного ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": None
                    },
                    'data': {
                        "crmReasonComment": '123gf'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": '123gf'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до null для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": '123gf'
                    },
                    'data': {
                        "crmReasonComment": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "crmReasonComment": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного ID из словаря до несуществующего ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": '123gf'
                    },
                    'data': {
                        "crmReasonComment": '123gf'
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
                    'name': 'Обновление сделки с валидного ID из словаря до вещественного ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": '123gf'
                    },
                    'data': {
                        "crmReasonComment": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": '12.08.2016'
                    },
                    'data': {
                        "crmReasonComment": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": None
                    },
                    'data': {
                        "crmReasonComment": 12.010
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
                    'name': 'Обновление сделки с null из словаря до '' ID из словаря для поля crmReasonComment',
                    'description': '',
                    'precondition': {
                        "crmReasonComment": None
                    },
                    'data': {
                        "crmReasonComment": ''
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
            "browserSignature": [
                {
                    'name': 'Обновление сделки с null до валидного поля из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": None
                    },
                    'data': {
                        "browserSignature": '123gf'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": '123gf'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": '123gf'
                    },
                    'data': {
                        "browserSignature": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "browserSignature": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до несуществующего ID из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": '123gf'
                    },
                    'data': {
                        "browserSignature": '123gf'
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
                    'name': 'Обновление сделки с валидного поля из словаря до вещественного числа из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": '123gf'
                    },
                    'data': {
                        "browserSignature": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного числа из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": '12.08.2016'
                    },
                    'data': {
                        "browserSignature": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного числа из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": None
                    },
                    'data': {
                        "browserSignature": 12.010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля browserSignature',
                    'description': '',
                    'precondition': {
                        "browserSignature": None
                    },
                    'data': {
                        "browserSignature": ''
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
            "actNumber": [
                {
                    'name': 'Обновление сделки с null до валидного поля из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": None
                    },
                    'data': {
                        "browserSignature": '123gf'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "actNumber": '123gf'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": '123gf'
                    },
                    'data': {
                        "actNumber": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "actNumber": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до несуществующего ID из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": '123gf'
                    },
                    'data': {
                        "actNumber": '123gf'
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
                    'name': 'Обновление сделки с валидного поля из словаря до вещественного числа из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": '123gf'
                    },
                    'data': {
                        "actNumber": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного числа из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": '12.08.2016'
                    },
                    'data': {
                        "actNumber": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного числа из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": None
                    },
                    'data': {
                        "actNumber": 12.010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля actNumber',
                    'description': '',
                    'precondition': {
                        "actNumber": None
                    },
                    'data': {
                        "actNumber": ''
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
            "additionalInfo": [
                {
                    'name': 'Обновление сделки с null до валидного поля из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": None
                    },
                    'data': {
                        "additionalInfo": '123gf'
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": '123gf'
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": '123gf'
                    },
                    'data': {
                        "additionalInfo": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "additionalInfo": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до несуществующего ID из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": '123gf'
                    },
                    'data': {
                        "additionalInfo": '123gf'
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
                    'name': 'Обновление сделки с валидного поля из словаря до вещественного числа из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": '123gf'
                    },
                    'data': {
                        "additionalInfo": 12.010
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
                    'name': 'Обновление сделки с валидного ID из словаря до целочисленного числа из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": '12.08.2016'
                    },
                    'data': {
                        "additionalInfo": 12010
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
                    'name': 'Обновление сделки с null из словаря до вещественного числа из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": None
                    },
                    'data': {
                        "additionalInfo": 12.010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля additionalInfo',
                    'description': '',
                    'precondition': {
                        "additionalInfo": None
                    },
                    'data': {
                        "additionalInfo": ''
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
            "approvedSum": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля approvedSum',
                    'description': '',
                    'precondition': {
                        "approvedSum": None
                    },
                    'data': {
                        "approvedSum": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля approvedSum',
                    'description': '',
                    'precondition': {
                        "approvedSum": 10.1
                    },
                    'data': {
                        "approvedSum": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "approvedSum": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля approvedSum',
                    'description': '',
                    'precondition': {
                        "approvedSum": 101.1
                    },
                    'data': {
                        "approvedSum": '123gf'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля approvedSum',
                    'description': '',
                    'precondition': {
                        "approvedSum": 12010.1
                    },
                    'data': {
                        "approvedSum": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля approvedSum',
                    'description': '',
                    'precondition': {
                        "approvedSum": None
                    },
                    'data': {
                        "approvedSum": ''
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
            "costFromEst": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля costFromEst',
                    'description': '',
                    'precondition': {
                        "costFromEst": None
                    },
                    'data': {
                        "costFromEst": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля costFromEst',
                    'description': '',
                    'precondition': {
                        "costFromEst": 10.1
                    },
                    'data': {
                        "costFromEst": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "costFromEst": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля costFromEst',
                    'description': '',
                    'precondition': {
                        "costFromEst": 101.1
                    },
                    'data': {
                        "costFromEst": '123gf'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля costFromEst',
                    'description': '',
                    'precondition': {
                        "costFromEst": 12010.1
                    },
                    'data': {
                        "costFromEst": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля costFromEst',
                    'description': '',
                    'precondition': {
                        "costFromEst": None
                    },
                    'data': {
                        "costFromEst": ''
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
            "initialFee ": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля initialFee ',
                    'description': '',
                    'precondition': {
                        "initialFee ": None
                    },
                    'data': {
                        "initialFee ": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee ": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля initialFee ',
                    'description': '',
                    'precondition': {
                        "initialFee ": 10.1
                    },
                    'data': {
                        "initialFee": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля initialFee ',
                    'description': '',
                    'precondition': {
                        "initialFee": 101.1
                    },
                    'data': {
                        "initialFee": '123gf'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля initialFee',
                    'description': '',
                    'precondition': {
                        "initialFee": 12010.1
                    },
                    'data': {
                        "initialFee": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля initialFee',
                    'description': '',
                    'precondition': {
                        "initialFeet": None
                    },
                    'data': {
                        "initialFee": ''
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
            "interestRate": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля interestRate',
                    'description': '',
                    'precondition': {
                        "interestRate": None
                    },
                    'data': {
                        "interestRate": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "interestRate": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля interestRate',
                    'description': '',
                    'precondition': {
                        "interestRate": 10.1
                    },
                    'data': {
                        "initialFee": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "initialFee": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля interestRate',
                    'description': '',
                    'precondition': {
                        "interestRate": 101.1
                    },
                    'data': {
                        "interestRate": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля interestRate',
                    'description': '',
                    'precondition': {
                        "interestRate": 12010.1
                    },
                    'data': {
                        "interestRate": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля interestRate',
                    'description': '',
                    'precondition': {
                        "interestRate": None
                    },
                    'data': {
                        "interestRate": ''
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
            "availableObjectDocuments": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": None
                    },
                    'data': {
                        "availableObjectDocuments": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": None
                    },
                    'data': {
                        "availableObjectDocuments": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": True
                    },
                    'data': {
                        "availableObjectDocuments": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": False
                    },
                    'data': {
                        "availableObjectDocuments": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "availableObjectDocuments": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": True
                    },
                    'data': {
                        "availableObjectDocuments": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": True
                    },
                    'data': {
                        "availableObjectDocuments": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": False
                    },
                    'data': {
                        "availableObjectDocuments": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": False
                    },
                    'data': {
                        "availableObjectDocuments": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": False
                    },
                    'data': {
                        "availableObjectDocuments": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": True
                    },
                    'data': {
                        "availableObjectDocuments": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля availableObjectDocuments',
                    'description': '',
                    'precondition': {
                        "availableObjectDocuments": None
                    },
                    'data': {
                        "availableObjectDocuments": ''
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
            "casAccessSend": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": None
                    },
                    'data': {
                        "casAccessSend": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": None
                    },
                    'data': {
                        "casAccessSend": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": True
                    },
                    'data': {
                        "casAccessSend": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": False
                    },
                    'data': {
                        "casAccessSend": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "casAccessSend": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": True
                    },
                    'data': {
                        "casAccessSend": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": True
                    },
                    'data': {
                        "casAccessSend": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": False
                    },
                    'data': {
                        "casAccessSend": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": False
                    },
                    'data': {
                        "casAccessSend": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": False
                    },
                    'data': {
                        "casAccessSend": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": True
                    },
                    'data': {
                        "casAccessSend": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля casAccessSend',
                    'description': '',
                    'precondition': {
                        "casAccessSend": None
                    },
                    'data': {
                        "casAccessSend": ''
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
            "cellDocumentSigned": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": None
                    },
                    'data': {
                        "cellDocumentSigned": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": None
                    },
                    'data': {
                        "cellDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": True
                    },
                    'data': {
                        "cellDocumentSigned": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": False
                    },
                    'data': {
                        "cellDocumentSigned": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "cellDocumentSigned": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": True
                    },
                    'data': {
                        "cellDocumentSigned": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": True
                    },
                    'data': {
                        "cellDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": False
                    },
                    'data': {
                        "cellDocumentSigned": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": False
                    },
                    'data': {
                        "cellDocumentSigned": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": False
                    },
                    'data': {
                        "cellDocumentSigned": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": True
                    },
                    'data': {
                        "cellDocumentSigned": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля cellDocumentSigned',
                    'description': '',
                    'precondition': {
                        "cellDocumentSigned": None
                    },
                    'data': {
                        "cellDocumentSigned": ''
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
            "copyExists": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": None
                    },
                    'data': {
                        "copyExists": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": None
                    },
                    'data': {
                        "copyExists": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": True
                    },
                    'data': {
                        "copyExists": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": False
                    },
                    'data': {
                        "copyExists": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "copyExists": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": True
                    },
                    'data': {
                        "copyExists": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": True
                    },
                    'data': {
                        "copyExists": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": False
                    },
                    'data': {
                        "copyExists": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": False
                    },
                    'data': {
                        "copyExists": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": False
                    },
                    'data': {
                        "copyExists": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": True
                    },
                    'data': {
                        "copyExists": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля copyExists',
                    'description': '',
                    'precondition': {
                        "copyExists": None
                    },
                    'data': {
                        "copyExists": ''
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
            "insuranceDocumentSigned": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": None
                    },
                    'data': {
                        "insuranceDocumentSigned": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": None
                    },
                    'data': {
                        "insuranceDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля c',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": True
                    },
                    'data': {
                        "insuranceDocumentSigned": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": False
                    },
                    'data': {
                        "insuranceDocumentSigned": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "insuranceDocumentSigned": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": True
                    },
                    'data': {
                        "insuranceDocumentSigned": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": True
                    },
                    'data': {
                        "insuranceDocumentSigned": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": False
                    },
                    'data': {
                        "insuranceDocumentSigned": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": False
                    },
                    'data': {
                        "insuranceDocumentSigned": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": False
                    },
                    'data': {
                        "insuranceDocumentSigned": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": True
                    },
                    'data': {
                        "insuranceDocumentSigned": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля insuranceDocumentSigned',
                    'description': '',
                    'precondition': {
                        "insuranceDocumentSigned": None
                    },
                    'data': {
                        "insuranceDocumentSigned": ''
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
            "isDraft": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": None
                    },
                    'data': {
                        "isDraft": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": None
                    },
                    'data': {
                        "isDraft": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": True
                    },
                    'data': {
                        "isDraft": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": False
                    },
                    'data': {
                        "isDraft": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isDraft": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": True
                    },
                    'data': {
                        "isDraft": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": True
                    },
                    'data': {
                        "isDraft": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": False
                    },
                    'data': {
                        "isDraft": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": False
                    },
                    'data': {
                        "isDraft": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": False
                    },
                    'data': {
                        "isDraft": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": True
                    },
                    'data': {
                        "isDraft": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля isDraft',
                    'description': '',
                    'precondition': {
                        "isDraft": None
                    },
                    'data': {
                        "isDraft": ''
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
            "wasDraft": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": None
                    },
                    'data': {
                        "wasDraft": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": None
                    },
                    'data': {
                        "wasDraft": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": True
                    },
                    'data': {
                        "wasDraft": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": False
                    },
                    'data': {
                        "wasDraft": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "wasDraft": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": True
                    },
                    'data': {
                        "wasDraft": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": True
                    },
                    'data': {
                        "wasDraft": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": False
                    },
                    'data': {
                        "wasDraft": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": False
                    },
                    'data': {
                        "wasDraft": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": False
                    },
                    'data': {
                        "wasDraft": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": True
                    },
                    'data': {
                        "wasDraft": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля wasDraft',
                    'description': '',
                    'precondition': {
                        "wasDraft": None
                    },
                    'data': {
                        "wasDraft": ''
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
            "isImported": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": None
                    },
                    'data': {
                        "isImported": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": None
                    },
                    'data': {
                        "isImported": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": True
                    },
                    'data': {
                        "isImported": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": False
                    },
                    'data': {
                        "isImported": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isImported": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": True
                    },
                    'data': {
                        "isImported": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": True
                    },
                    'data': {
                        "isImported": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": False
                    },
                    'data': {
                        "isImported": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": False
                    },
                    'data': {
                        "isImported": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": False
                    },
                    'data': {
                        "isImported": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": True
                    },
                    'data': {
                        "isImported": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля isImported',
                    'description': '',
                    'precondition': {
                        "isImported": None
                    },
                    'data': {
                        "isImported": ''
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
            "isMorton ": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isMorton ',
                    'description': '',
                    'precondition': {
                        "isMorton": None
                    },
                    'data': {
                        "isMorton": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": None
                    },
                    'data': {
                        "isMorton": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": True
                    },
                    'data': {
                        "isMorton": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": False
                    },
                    'data': {
                        "isMorton": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isMorton": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": True
                    },
                    'data': {
                        "isMorton": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": True
                    },
                    'data': {
                        "isMorton": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": False
                    },
                    'data': {
                        "isMorton": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": False
                    },
                    'data': {
                        "isMorton": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": False
                    },
                    'data': {
                        "isMorton": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": True
                    },
                    'data': {
                        "isMorton": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля isMorton',
                    'description': '',
                    'precondition': {
                        "isMorton": None
                    },
                    'data': {
                        "isMorton": ''
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
            "isPortalLogin": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isPortalLogin ',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": None
                    },
                    'data': {
                        "isPortalLogin": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": None
                    },
                    'data': {
                        "isPortalLogin": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": True
                    },
                    'data': {
                        "isPortalLogin": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": False
                    },
                    'data': {
                        "isPortalLogin": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isPortalLogin": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": True
                    },
                    'data': {
                        "isPortalLogin": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": True
                    },
                    'data': {
                        "isPortalLogin": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": False
                    },
                    'data': {
                        "isPortalLogin": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": False
                    },
                    'data': {
                        "isPortalLogin": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": False
                    },
                    'data': {
                        "isPortalLogin": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": True
                    },
                    'data': {
                        "isPortalLogin": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля isPortalLogin',
                    'description': '',
                    'precondition': {
                        "isPortalLogin": None
                    },
                    'data': {
                        "isPortalLogin": ''
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
            "isUrm": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isUrm ',
                    'description': '',
                    'precondition': {
                        "isUrm": None
                    },
                    'data': {
                        "isUrm": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": None
                    },
                    'data': {
                        "isUrm": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": True
                    },
                    'data': {
                        "isUrm": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": False
                    },
                    'data': {
                        "isUrm": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "isUrm": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": True
                    },
                    'data': {
                        "isUrm": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": True
                    },
                    'data': {
                        "isUrm": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": False
                    },
                    'data': {
                        "isUrm": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": False
                    },
                    'data': {
                        "isUrm": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": False
                    },
                    'data': {
                        "isUrm": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": True
                    },
                    'data': {
                        "isUrm": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля isUrm',
                    'description': '',
                    'precondition': {
                        "isUrm": None
                    },
                    'data': {
                        "isUrm": ''
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
            "plannedBorrow": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля plannedBorrow ',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": None
                    },
                    'data': {
                        "plannedBorrow": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": None
                    },
                    'data': {
                        "plannedBorrow": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": True
                    },
                    'data': {
                        "plannedBorrow": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "plannedBorrow": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": False
                    },
                    'data': {
                        'expected': {
                            "success": True,
                            "data": [{
                                "dealStatusId": 8060,
                                "plannedBorrow": None
                            }]
                        }
                    },
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": True
                    },
                    'data': {
                        "plannedBorrow": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": True
                    },
                    'data': {
                        "plannedBorrow": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": False
                    },
                    'data': {
                        "plannedBorrow": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": False
                    },
                    'data': {
                        "plannedBorrow": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": False
                    },
                    'data': {
                        "plannedBorrow": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": True
                    },
                    'data': {
                        "plannedBorrow": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля plannedBorrow',
                    'description': '',
                    'precondition': {
                        "plannedBorrow": None
                    },
                    'data': {
                        "plannedBorrow": ''
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
            "propertyApproval": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля propertyApproval ',
                    'description': '',
                    'precondition': {
                        "propertyApproval": None
                    },
                    'data': {
                        "propertyApproval": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": None
                    },
                    'data': {
                        "propertyApproval": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": True
                    },
                    'data': {
                        "propertyApproval": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "propertyApproval": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": False
                    },
                    'data': {
                        'expected': {
                            "success": True,
                            "data": [{
                                "dealStatusId": 8060,
                                "propertyApproval": None
                            }]
                        }
                    },
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": True
                    },
                    'data': {
                        "propertyApproval": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": True
                    },
                    'data': {
                        "propertyApproval": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": False
                    },
                    'data': {
                        "propertyApproval": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": False
                    },
                    'data': {
                        "propertyApproval": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": False
                    },
                    'data': {
                        "propertyApproval": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": True
                    },
                    'data': {
                        "propertyApproval": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля propertyApproval',
                    'description': '',
                    'precondition': {
                        "propertyApproval": None
                    },
                    'data': {
                        "propertyApproval": ''
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
            "recovered": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля recovered ',
                    'description': '',
                    'precondition': {
                        "recovered": None
                    },
                    'data': {
                        "recovered": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": None
                    },
                    'data': {
                        "recovered": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": True
                    },
                    'data': {
                        "recovered": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": False
                    },
                    'data': {},
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "recovered": None
                        }]
                    },
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": True
                    },
                    'data': {
                        "recovered": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": True
                    },
                    'data': {
                        "recovered": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": False
                    },
                    'data': {
                        "recovered": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": False
                    },
                    'data': {
                        "recovered": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": False
                    },
                    'data': {
                        "recovered": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": True
                    },
                    'data': {
                        "recovered": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля recovered',
                    'description': '',
                    'precondition': {
                        "recovered": None
                    },
                    'data': {
                        "recovered": ''
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
            "urmCik": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля urmCik ',
                    'description': '',
                    'precondition': {
                        "urmCik": None
                    },
                    'data': {
                        "urmCik": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": None
                    },
                    'data': {
                        "urmCik": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": True
                    },
                    'data': {
                        "urmCik": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": False
                    },
                    'data': {},
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "urmCik": None
                        }]
                    },
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": True
                    },
                    'data': {
                        "urmCik": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": True
                    },
                    'data': {
                        "urmCik": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": False
                    },
                    'data': {
                        "urmCik": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": False
                    },
                    'data': {
                        "urmCik": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": False
                    },
                    'data': {
                        "urmCik": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": True
                    },
                    'data': {
                        "urmCik": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля urmCik',
                    'description': '',
                    'precondition': {
                        "urmCik": None
                    },
                    'data': {
                        "urmCik": ''
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
            "viewOnlyForOwner": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": None
                    },
                    'data': {
                        "viewOnlyForOwner": True
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "viewOnlyForOwner": 8060,
                            "urmCik": True
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": None
                    },
                    'data': {
                        "viewOnlyForOwner": False
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": False
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": True
                    },
                    'data': {
                        "viewOnlyForOwner": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": False
                    },
                    'data': {},
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "viewOnlyForOwner": None
                        }]
                    },
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": True
                    },
                    'data': {
                        "viewOnlyForOwner": '123%'
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
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": True
                    },
                    'data': {
                        "viewOnlyForOwner": False
                    },
                    'expected': {
                        "success": True,
                        "errors": [
                            {
                                "code": 400,
                                "userMessage": None,
                            }
                        ]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля на валидное из словаря до строки из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": False
                    },
                    'data': {
                        "viewOnlyForOwner": True
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
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": False
                    },
                    'data': {
                        "viewOnlyForOwner": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": False
                    },
                    'data': {
                        "viewOnlyForOwner": 12010
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": True
                    },
                    'data': {
                        "viewOnlyForOwner": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля viewOnlyForOwner',
                    'description': '',
                    'precondition': {
                        "viewOnlyForOwner": None
                    },
                    'data': {
                        "viewOnlyForOwner": ''
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
            "issuedSum": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля issuedSum',
                    'description': '',
                    'precondition': {
                        "issuedSum": None
                    },
                    'data': {
                        "issuedSum": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля issuedSum',
                    'description': '',
                    'precondition': {
                        "issuedSum": 10.1
                    },
                    'data': {
                        "issuedSum": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "issuedSum": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля issuedSum',
                    'description': '',
                    'precondition': {
                        "issuedSum": 101.1
                    },
                    'data': {
                        "issuedSum": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля issuedSum',
                    'description': '',
                    'precondition': {
                        "issuedSum": 12010.1
                    },
                    'data': {
                        "issuedSum": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля issuedSum',
                    'description': '',
                    'precondition': {
                        "issuedSum": None
                    },
                    'data': {
                        "issuedSum": ''
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
            "monthlyPayment": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля monthlyPayment',
                    'description': '',
                    'precondition': {
                        "monthlyPayment": None
                    },
                    'data': {
                        "monthlyPayment": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля monthlyPayment',
                    'description': '',
                    'precondition': {
                        "monthlyPayment": 10.1
                    },
                    'data': {
                        "monthlyPayment": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "monthlyPayment": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля monthlyPayment',
                    'description': '',
                    'precondition': {
                        "monthlyPayment": 101.1
                    },
                    'data': {
                        "monthlyPayment": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля monthlyPayment',
                    'description': '',
                    'precondition': {
                        "monthlyPayment": 12010.1
                    },
                    'data': {
                        "monthlyPayment": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля monthlyPayment',
                    'description': '',
                    'precondition': {
                        "monthlyPayment": None
                    },
                    'data': {
                        "monthlyPayment": ''
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
            "neededRevenue": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля neededRevenue',
                    'description': '',
                    'precondition': {
                        "neededRevenue": None
                    },
                    'data': {
                        "neededRevenue": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля neededRevenue',
                    'description': '',
                    'precondition': {
                        "neededRevenue": 10.1
                    },
                    'data': {
                        "neededRevenue": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "neededRevenue": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля neededRevenue',
                    'description': '',
                    'precondition': {
                        "neededRevenue": 101.1
                    },
                    'data': {
                        "neededRevenue": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля neededRevenue',
                    'description': '',
                    'precondition': {
                        "neededRevenue": 12010.1
                    },
                    'data': {
                        "neededRevenue": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля neededRevenue',
                    'description': '',
                    'precondition': {
                        "neededRevenue": None
                    },
                    'data': {
                        "neededRevenue": ''
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
            "objectLivingSpace": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля objectLivingSpace',
                    'description': '',
                    'precondition': {
                        "objectLivingSpace": None
                    },
                    'data': {
                        "objectLivingSpace": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля objectLivingSpace',
                    'description': '',
                    'precondition': {
                        "objectLivingSpace": 10.1
                    },
                    'data': {
                        "objectLivingSpace": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectLivingSpace": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля objectLivingSpace',
                    'description': '',
                    'precondition': {
                        "objectLivingSpace": 101.1
                    },
                    'data': {
                        "objectLivingSpace": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля objectLivingSpace',
                    'description': '',
                    'precondition': {
                        "objectLivingSpace": 12010.1
                    },
                    'data': {
                        "objectLivingSpace": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля objectLivingSpace',
                    'description': '',
                    'precondition': {
                        "objectLivingSpace": None
                    },
                    'data': {
                        "objectLivingSpace": ''
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
            "objectSpace": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля objectSpace',
                    'description': '',
                    'precondition': {
                        "objectSpace": None
                    },
                    'data': {
                        "objectSpace": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля objectSpace',
                    'description': '',
                    'precondition': {
                        "objectSpace": 10.1
                    },
                    'data': {
                        "objectSpace": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "objectSpace": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля objectSpace',
                    'description': '',
                    'precondition': {
                        "objectSpace": 101.1
                    },
                    'data': {
                        "objectSpace": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля objectSpace',
                    'description': '',
                    'precondition': {
                        "objectSpace": 12010.1
                    },
                    'data': {
                        "objectSpace": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля objectSpace',
                    'description': '',
                    'precondition': {
                        "objectSpace": None
                    },
                    'data': {
                        "objectSpace": ''
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
            "requestedSum": [
                {
                    'name': 'Обновление сделки с null до валидного значения из словаря для поля requestedSum',
                    'description': '',
                    'precondition': {
                        "requestedSum": None
                    },
                    'data': {
                        "requestedSum": 101.45
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": 101.45
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до null для поля requestedSum',
                    'description': '',
                    'precondition': {
                        "requestedSum": 10.1
                    },
                    'data': {
                        "requestedSum": None
                    },
                    'expected': {
                        "success": True,
                        "data": [{
                            "dealStatusId": 8060,
                            "requestedSum": None
                        }]
                    }
                },
                {
                    'name': 'Обновление сделки с валидного поля из словаря до строки из словаря для поля requestedSum',
                    'description': '',
                    'precondition': {
                        "requestedSum": 101.1
                    },
                    'data': {
                        "requestedSum": '123%'
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
                    'name': 'Обновление сделки с валидного значения из словаря до целочисленного числа из словаря для поля requestedSum',
                    'description': '',
                    'precondition': {
                        "requestedSum": 12010.1
                    },
                    'data': {
                        "requestedSum": 12010
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
                    'name': 'Обновление сделки с null из словаря до ''  из словаря для поля requestedSum',
                    'description': '',
                    'precondition': {
                        "requestedSum": None
                    },
                    'data': {
                        "requestedSum": ''
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
}