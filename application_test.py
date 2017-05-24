import application_data
import lib
import pytest


@pytest.mark.application
@pytest.mark.parametrize("ddt",
                         application_data.delete
                         )
def test_application_delete(ddt):
    if ddt['precondition']['create_application']:
        deal_id, application_id = lib.su_status('100', 's-101')
    elif 'data' in ddt['precondition']:
        application_id = ddt['precondition']['data']['applicationId']
    else:
        raise Exception('Не может быть получен ID документа')
    if ddt['precondition']['delete_application']:
        lib.delete_application(application_id)
    resp = lib.delete_application(application_id)
    if 'json' in ddt['expected'].keys():
        result = lib.json_include(ddt['expected']['json'], resp.json(), verbose=False)
    elif 'sql' in ddt['expected'].keys():
        sql_request = ddt['expected']['sql']['request'] % str(application_id)
        result = ddt['expected']['sql']['result'] == lib.make_sql_request(sql_request)
    else:
        raise Exception('Не указан тип ожидаемого результата')
    assert result is True