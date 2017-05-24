import event_data
import lib
import pytest
import time

@pytest.mark.event
@pytest.mark.parametrize("ddt", event_data.rejection_reason)
def test_event_fields_post(ddt):
    # time.sleep(1)
    if ddt['precondition']['create_deal']:
        deal_id, application_id = lib.su_status('100', 's-0')
    elif 'data' in ddt['precondition']:
        deal_id = ddt['precondition']['data']['dealId']
    else:
        raise Exception('Не может быть получен ID документа')
    if ddt['precondition']['delete_deal']:
        lib.delete_deal(deal_id)
    resp = lib.post_event(deal_id=deal_id, j=ddt['data'])
    print(resp.json())
    if 'json' in ddt['expected'].keys():
        result = lib.json_include(ddt['expected']['json'], resp.json(), verbose=False)
    elif 'sql' in ddt['expected'].keys():
        sql_request = ddt['expected']['sql']['request'] % str(resp.json()['data'][0]['id'])
        result = ddt['expected']['sql']['result'] == lib.make_sql_request(sql_request)
    else:
        raise Exception('Не указан тип ожидаемого результата')

    assert result is True