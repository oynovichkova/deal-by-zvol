dictionary = {
    'get_validation': {
        "dictionary_tests": [
            {
                'name': 'Отдаётся корректный словарь по корректно указанному типу',
                'description': '',
                'data': {
                    'dictionary_type': 'dict_mp_job_organization_type',
                },
                'expected': {
                    "success": True,
                    "dictionaries": {
                        "dict_mp_job_organization_type": [
                            {
                                "id": 5090,
                                "title": "ТУРИЗМ",
                                "type": "dict_mp_job_organization_type",
                                "order": 90,
                                "comment": ""
                            },
                            {
                                "id": 5160,
                                "title": "СТРОИТЕЛЬСТВО",
                                "type": "dict_mp_job_organization_type",
                                "order": 160,
                                "comment": ""
                            },
                            {
                                "id": 5020,
                                "title": "КОНСАЛТИНГОВЫЕ УСЛУГИ",
                                "type": "dict_mp_job_organization_type",
                                "order": 20,
                                "comment": ""
                            },
                            {
                                "id": 5050,
                                "title": "ПРЕДПРИЯТИЯ ТЭК",
                                "type": "dict_mp_job_organization_type",
                                "order": 50,
                                "comment": ""
                            },
                            {
                                "id": 5120,
                                "title": "КУЛЬТУРА И ИСКУССТВО",
                                "type": "dict_mp_job_organization_type",
                                "order": 120,
                                "comment": ""
                            },
                            {
                                "id": 5010,
                                "title": "ФИНАНСЫ, БАНКИ, СТРАХОВАНИЕ",
                                "type": "dict_mp_job_organization_type",
                                "order": 10,
                                "comment": ""
                            },
                            {
                                "id": 5080,
                                "title": "ОХРАННАЯ ДЕЯТЕЛЬНОСТЬ",
                                "type": "dict_mp_job_organization_type",
                                "order": 80,
                                "comment": ""
                            },
                            {
                                "id": 5190,
                                "title": "ДРУГИЕ ОТРАСЛИ",
                                "type": "dict_mp_job_organization_type",
                                "order": 190,
                                "comment": ""
                            },
                            {
                                "id": 5040,
                                "title": "ПРОМЫШЛЕННОСТЬ И МАШИНОСТОЕНИЕ",
                                "type": "dict_mp_job_organization_type",
                                "order": 40,
                                "comment": ""
                            },
                            {
                                "id": 5150,
                                "title": "ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ / ТЕЛЕКОММУНИКАЦИИ",
                                "type": "dict_mp_job_organization_type",
                                "order": 150,
                                "comment": ""
                            },
                            {
                                "id": 5110,
                                "title": "МЕДИЦИНА",
                                "type": "dict_mp_job_organization_type",
                                "order": 110,
                                "comment": ""
                            },
                            {
                                "id": 5180,
                                "title": "ОПТОВАЯ/РОЗНИЧНАЯ ТОРГОВЛЯ",
                                "type": "dict_mp_job_organization_type",
                                "order": 180,
                                "comment": ""
                            },
                            {
                                "id": 5070,
                                "title": "ТРАНСПОРТ",
                                "type": "dict_mp_job_organization_type",
                                "order": 70,
                                "comment": ""
                            },
                            {
                                "id": 5140,
                                "title": "СОЦИАЛЬНАЯ СФЕРА",
                                "type": "dict_mp_job_organization_type",
                                "order": 140,
                                "comment": ""
                            },
                            {
                                "id": 5170,
                                "title": "НАУКА",
                                "type": "dict_mp_job_organization_type",
                                "order": 170,
                                "comment": ""
                            },
                            {
                                "id": 5030,
                                "title": "АРМИЯ",
                                "type": "dict_mp_job_organization_type",
                                "order": 30,
                                "comment": ""
                            },
                            {
                                "id": 5100,
                                "title": "ОБРАЗОВАНИЕ",
                                "type": "dict_mp_job_organization_type",
                                "order": 100,
                                "comment": ""
                            },
                            {
                                "id": 5130,
                                "title": "ОРГАНЫ ВЛАСТИ И УПРАВЛЕНИЯ",
                                "type": "dict_mp_job_organization_type",
                                "order": 130,
                                "comment": ""
                            },
                            {
                                "id": 5200,
                                "title": "УСЛУГИ",
                                "type": "dict_mp_job_organization_type",
                                "order": 200,
                                "comment": ""
                            },
                            {
                                "id": 5060,
                                "title": "МЕТАЛЛУРГИЯ",
                                "type": "dict_mp_job_organization_type",
                                "order": 60,
                                "comment": ""
                            }
                        ]
                    },
                    "data": []
                }
            },
            {
                'name': 'Ошибка по несуществующему типу словаря',
                'description': '',
                'data': {
                    'dictionary_type': 'some_error_type',
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "code": 404,
                            "internalMessage" : "ResourceNotFoundException: No results for requested types[some_test_dictionary]",
                            "userMessage": None,
                        }
                    ]
                }
            },
        ],
        "subset_tests": [
            {
                'name': 'Отдаётся корректный словарь по корректно указанному типу с указанной фильтрацией',
                'description': '',
                'data': {
                    'dictionary_type': 'dict_deal_product_type',
                    'dependentById': '11020',
                },
                'expected': {
                    "success": True,
                    "dictionaries": {
                        "dict_deal_product_type": [
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15020,
                                "title": "Материнский капитал",
                                "type": "dict_deal_product_type",
                                "order": 20,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15130,
                                "title": "Загородная недвижимость",
                                "type": "dict_deal_product_type",
                                "order": 120,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15030,
                                "title": "Рефинансирование",
                                "type": "dict_deal_product_type",
                                "order": 30,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15140,
                                "title": "Строительство жилого дома",
                                "type": "dict_deal_product_type",
                                "order": 130,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15110,
                                "title": "Приобретение готового жилья",
                                "type": "dict_deal_product_type",
                                "order": 100,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15090,
                                "title": "Отдельные программы и соглашения",
                                "type": "dict_deal_product_type",
                                "order": 80,
                                "comment": ""
                            },
                            {
                                "createdTime": "2016-10-19T14:08:51.203Z",
                                "modifiedTime": "2016-10-19T14:08:51.203Z",
                                "modifiedBy": 0,
                                "id": 15120,
                                "title": "Приобретение строящегося жилья",
                                "type": "dict_deal_product_type",
                                "order": 110,
                                "comment": ""
                            }
                        ]
                    },
                    "data": []
                }
            },
            {
                'name': 'Ошибка по несуществующему типу словаря с фильтрацией',
                'description': '',
                'data': {
                    'dictionary_type': 'some_error_type',
                    'dependentById': '11020',
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "code": 404,
                            "internalMessage": "ResourceNotFoundException: No results for requested type and id: some_error_type 11020",
                            "userMessage": None,
                        }
                    ]
                }
            },
            {
                'name': 'Ошибка по существующему типу словаря и несуществующему фильтру',
                'description': '',
                'data': {
                    'dictionary_type': 'dict_deal_product_type',
                    'dependentById': '1102',
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "code": 404,
                            "internalMessage": "ResourceNotFoundException: No results for requested type: dict_deal_product_type",
                            "userMessage": None,
                        }
                    ]
                }
            },
{
                'name': 'Ошибка по существующему типу словаря и несуществующему фильтру',
                'description': '',
                'data': {
                    'dictionary_type': 'dict_deal_product_type',
                    'dependentById': '1102',
                },
                'expected': {
                    "success": False,
                    "errors": [
                        {
                            "code": 404,
                            "internalMessage": "ResourceNotFoundException: No results for requested type: dict_deal_product_type",
                            "userMessage": None,
                        }
                    ]
                }
            },
        ],
    },
}