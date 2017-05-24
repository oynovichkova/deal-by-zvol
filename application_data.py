delete = [
    {
        'name': 'Архивирование существующей анкеты',
        'description': '',
        'precondition': {
            "create_application": True,
            "delete_application": False,
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
        'name': 'Архивирование существующей анкеты с проверкой выставляемого флага в базе',
        'description': '',
        'precondition': {
            "create_application": True,
            "delete_application": False,
        },
        'data': {},
        'expected': {
            'sql': {
                'request': 'SELECT archived FROM application WHERE id=%s',
                'result': [(True,)]
            }
        }
    },
    {
        'name': 'Повторное архивирование существующей анкеты',
        'description': '',
        'precondition': {
            "create_application": True,
            "delete_application": True,
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
        'name': 'Архивирование несуществующей анкеты',
        'description': '',
        'precondition': {
            "create_application": False,
            "delete_application": False,
            'data': {
                'applicationId': 123123123123123,
            },
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
        'name': 'Удаление нескольких анкет',
        'description': '',
        'precondition': {
            "create_application": False,
            "delete_application": False,
            'data': {
                'applicationId': '52,53',
            },
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

sql_application = {
    'create': {
        'application': '',
        'accounting': '',
        'relations': '',
        'sberAccounts': '',
        'sberCards': '',
        'vehicle': '',
        'registrationAdress': '',
        'actualAdress': '',
        'tempRegistrationAdress': ''
    }
}

full_application = {
    "accountNumber": "12345678901234567890",
    "accountingItems": [
        {
            "accountingType": "PROOF_INCOME",
            "sum": 125000.00
        }
    ],
    "actualAddress": {
        "suggestion": {
            "data": {
                "city": "Химки",
                "flat": "4",
                "house": "5А",
                "okato": "46483000000",
                "oktmo": "46783000",
                "qc_geo": "1",
                "region": "Московская",
                "street": "Горшина",
                "country": "Россия",
                "fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "geo_lat": "55.8856849",
                "geo_lon": "37.4315753",
                "kladr_id": "5000003000000880021",
                "city_type": "г",
                "flat_type": "кв",
                "fias_level": "8",
                "house_type": "д",
                "tax_office": "5047",
                "postal_code": "141407",
                "region_type": "обл",
                "street_type": "ул",
                "city_fias_id": "d76255c8-3173-4db5-a39b-badd3ebdf851",
                "city_kladr_id": "5000003000000",
                "house_fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "capital_marker": "0",
                "city_type_full": "город",
                "city_with_type": "г Химки",
                "flat_type_full": "квартира",
                "house_kladr_id": "5000003000000880021",
                "region_fias_id": "29251dcf-00a1-4e34-98d4-5c47484a36d4",
                "street_fias_id": "141f4a91-6539-4100-aa6e-57857cde4ae7",
                "house_type_full": "дом",
                "region_kladr_id": "5000000000000",
                "street_kladr_id": "50000030000008800",
                "region_type_full": "область",
                "region_with_type": "Московская обл",
                "street_type_full": "улица",
                "street_with_type": "ул Горшина"
            },
            "value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4",
            "unrestricted_value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4"
        }
    },
    "actualLiveInCityYears": 12,
    "actualLiveTypeId": 7050,
    "actualLiveYears": 5,
    "applicationStatus": "DRAFT",
    "applicationType": "BORROWER",
    "applicationTypePledger": True,
    "canConfirmIncome": True,
    "casId": 1,
    "considerCoBorrowerIncome": True,
    "contactMail": "test@example.com",
    "contactPhoneHome": "4951230099",
    "contactPhoneMobile": "9263332211",
    "contactPhoneRegister": "4991234567",
    "contactPhoneReserved": "4950123456",
    "contactPhoneReservedType": "MOBILE",
    "contactPhoneWork": "4981112233",
    "creditHistorySubjectCode": "КР-48769",
    "dealId": None,
    "educationCourse": 4,
    "educationType": "HIGHER_EDUCATION_COMPLETED",
    "haveChildren": True,
    "individualInsuranceNumber": "ИСН-1231-12",
    "individualProprietor": True,
    "isIndividualProprietor": False,
    "isSalaryViaSber": True,
    "isSpouseYounger35": True,
    "jobCategoryId": 1030,
    "jobChangesCount": 0,
    "jobDurationId": 3070,
    "jobFirstSignRight": True,
    "jobOrganization": "ООО Могильные сети",
    "jobOrganizationClarification": "Организация могильной связи",
    "jobOrganizationInn": "123456787032",
    "jobOrganizationTypeId": 5150,
    "jobOwnPercent": 1,
    "jobPosition": "Главный управляющий по могильной связи",
    "jobPrivatePracticeClarification": "Верховный лич",
    "jobSeniorityId": 7240,
    "jobStaffId": 2050,
    "jobTypeId": 4030,
    "mandatoryCoBorrower": False,
    "marriageContract": True,
    "marriageStatus": "MARRIED",
    "minorsAmount": 2,
    "passportForeignValid": True,
    "passportIssueDate": "2000-03-13TZ",
    "passportIssuer": "УФМС города Нска №3184",
    "passportNumber": "123456",
    "passportSeries": "1234",
    "passportSubdivisionCode": "Н-3184",
    "personBirthPlace": "Больше Кукуево, Россия",
    "personBirthday": "1964-10-31TZ",
    "personFirstName": "Василий",
    "personGender": "MALE",
    "personInn": "123456786790",
    "personLastName": "Пупкин",
    "personMiddleName": "Татьянович",
    "realtyItems": [
        {
            "area": 250,
            "marketPrice": 120000000.00,
            "realtyTypeId": 6010,
            "region": {
                "suggestion": {
                    "data": {
                        "city": "Химки",
                        "flat": "4",
                        "house": "5А",
                        "okato": "46483000000",
                        "oktmo": "46783000",
                        "qc_geo": "1",
                        "region": "Московская",
                        "street": "Горшина",
                        "country": "Россия",
                        "fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                        "geo_lat": "55.8856849",
                        "geo_lon": "37.4315753",
                        "kladr_id": "5000003000000880021",
                        "city_type": "г",
                        "flat_type": "кв",
                        "fias_level": "8",
                        "house_type": "д",
                        "tax_office": "5047",
                        "postal_code": "141407",
                        "region_type": "обл",
                        "street_type": "ул",
                        "city_fias_id": "d76255c8-3173-4db5-a39b-badd3ebdf851",
                        "city_kladr_id": "5000003000000",
                        "house_fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                        "capital_marker": "0",
                        "city_type_full": "город",
                        "city_with_type": "г Химки",
                        "flat_type_full": "квартира",
                        "house_kladr_id": "5000003000000880021",
                        "region_fias_id": "29251dcf-00a1-4e34-98d4-5c47484a36d4",
                        "street_fias_id": "141f4a91-6539-4100-aa6e-57857cde4ae7",
                        "house_type_full": "дом",
                        "region_kladr_id": "5000000000000",
                        "street_kladr_id": "50000030000008800",
                        "region_type_full": "область",
                        "region_with_type": "Московская обл",
                        "street_type_full": "улица",
                        "street_with_type": "ул Горшина"
                    },
                    "value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4",
                    "unrestricted_value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4"
                }
            },
            "yearOfPurchase": 2015
        }
    ],
    "registrationAddress": {
        "suggestion": {
            "data": {
                "city": "Химки",
                "flat": "4",
                "house": "5А",
                "okato": "46483000000",
                "oktmo": "46783000",
                "qc_geo": "1",
                "region": "Московская",
                "street": "Горшина",
                "country": "Россия",
                "fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "geo_lat": "55.8856849",
                "geo_lon": "37.4315753",
                "kladr_id": "5000003000000880021",
                "city_type": "г",
                "flat_type": "кв",
                "fias_level": "8",
                "house_type": "д",
                "tax_office": "5047",
                "postal_code": "141407",
                "region_type": "обл",
                "street_type": "ул",
                "city_fias_id": "d76255c8-3173-4db5-a39b-badd3ebdf851",
                "city_kladr_id": "5000003000000",
                "house_fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "capital_marker": "0",
                "city_type_full": "город",
                "city_with_type": "г Химки",
                "flat_type_full": "квартира",
                "house_kladr_id": "5000003000000880021",
                "region_fias_id": "29251dcf-00a1-4e34-98d4-5c47484a36d4",
                "street_fias_id": "141f4a91-6539-4100-aa6e-57857cde4ae7",
                "house_type_full": "дом",
                "region_kladr_id": "5000000000000",
                "street_kladr_id": "50000030000008800",
                "region_type_full": "область",
                "region_with_type": "Московская обл",
                "street_type_full": "улица",
                "street_with_type": "ул Горшина"
            },
            "value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4",
            "unrestricted_value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4"
        }
    },
    "relationsItems": [
        {
            "birthday": "1953-06-09TZ",
            "firstName": "Иван",
            "lastName": "Иванов",
            "middleName": "Иванович",
            "relationsType": "HUSBAND",
            "sberbankSubdivision": "ЦА"
        }
    ],
    "renameFirstName": "Абдурахман",
    "renameLastName": "Хаттаб",
    "renameMiddleName": "ибн",
    "renameOccurred": "1998-01-01TZ",
    "renameReason": "OTHER",
    "renameReasonOther": "По причине неблагозвучности",
    "salaryViaSber": True,
    "sberAccountItems": [
        {
            "number": "12345678901234567890",
            "serviceType": "SALARY"
        }
    ],
    "sberCardItems": [
        {
            "number": "4513515464545435",
            "serviceType": "SALARY"
        }
    ],
    "spouseYounger35": True,
    "tempRegistrationAddress": {
        "suggestion": {
            "data": {
                "city": "Химки",
                "flat": "4",
                "house": "5А",
                "okato": "46483000000",
                "oktmo": "46783000",
                "qc_geo": "1",
                "region": "Московская",
                "street": "Горшина",
                "country": "Россия",
                "fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "geo_lat": "55.8856849",
                "geo_lon": "37.4315753",
                "kladr_id": "5000003000000880021",
                "city_type": "г",
                "flat_type": "кв",
                "fias_level": "8",
                "house_type": "д",
                "tax_office": "5047",
                "postal_code": "141407",
                "region_type": "обл",
                "street_type": "ул",
                "city_fias_id": "d76255c8-3173-4db5-a39b-badd3ebdf851",
                "city_kladr_id": "5000003000000",
                "house_fias_id": "73da2ab0-40bc-405d-8b18-3105f1cab79d",
                "capital_marker": "0",
                "city_type_full": "город",
                "city_with_type": "г Химки",
                "flat_type_full": "квартира",
                "house_kladr_id": "5000003000000880021",
                "region_fias_id": "29251dcf-00a1-4e34-98d4-5c47484a36d4",
                "street_fias_id": "141f4a91-6539-4100-aa6e-57857cde4ae7",
                "house_type_full": "дом",
                "region_kladr_id": "5000000000000",
                "street_kladr_id": "50000030000008800",
                "region_type_full": "область",
                "region_with_type": "Московская обл",
                "street_type_full": "улица",
                "street_with_type": "ул Горшина"
            },
            "value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4",
            "unrestricted_value": "Московская обл, г Химки, ул Горшина, д 5А, кв 4"
        }
    },
    "tempRegistrationUntil": "2016-12-01TZ",
    "vehicleItems": [
        {
            "marketPrice": 500000.0,
            "model": "Nissan NP-500",
            "regNumber": "А123ММ777",
            "vehicleType": "LAND",
            "yearOfPurchase": 2012,
            "yearsOld": 15
        }
    ]
}