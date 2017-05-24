rejection_reason = [
    {
        'name': 'Проверка сохранения в базе корректного Rejection Reason ID при отправке события',
        'description': '',
        'precondition': {
            "create_deal": True,
            "delete_deal": False,
        },
        'data': {
            'event': 'BORROWER_APPROVAL_EXPIRED',
            'rejectionReasonId': 10030,
        },
        'expected': {
            'sql': {
                'request': 'SELECT rejection_reason_id FROM deal_history WHERE id=%s',
                'result': [(10030,)]
            }
        }
    },
    {
        'name': 'Проверка сохранения в базе корректного Comment при отправке события',
        'description': '',
        'precondition': {
            "create_deal": True,
            "delete_deal": False,
        },
        'data': {
            'event': 'BORROWER_APPROVAL_EXPIRED',
            'comment': "Проверка комментария к переходу по сделке",
        },
        'expected': {
            'sql': {
                'request': 'SELECT comment FROM deal_history WHERE id=%s',
                'result': [("Проверка комментария к переходу по сделке",)]
            }
        }
    },
]