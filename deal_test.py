import deal_data
import lib
import pytest


@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         deal_data.delete
                         )
def test_deal_delete(ddt):
    if ddt['precondition']['create_deal']:
        deal_id, application_id = lib.su_status('100', 's-0')
    elif 'data' in ddt['precondition']:
        deal_id = ddt['precondition']['data']['dealId']
    else:
        raise Exception('Не может быть получен ID документа')
    if ddt['precondition']['delete_deal']:
        lib.delete_deal(deal_id)
    resp = lib.delete_deal(deal_id)
    if 'json' in ddt['expected'].keys():
        result = lib.json_include(ddt['expected']['json'], resp.json(), verbose=False)
    elif 'sql' in ddt['expected'].keys():
        sql_request = ddt['expected']['sql']['request'] % str(deal_id)
        result = ddt['expected']['sql']['result'] == lib.make_sql_request(sql_request)
    else:
        raise Exception('Не указан тип ожидаемого результата')

    assert result is True


@pytest.mark.pagination
@pytest.mark.parametrize("ddt",
                         deal_data.pagination['negative']
                         )
def test_pagination_negative(ddt):
    resp = lib.get_deal_by_user_id(page=ddt['data']['page'],
                                   size=ddt['data']['size'])
    result = lib.json_include(ddt['expected'], resp.json(), verbose=False)
    assert result is True


@pytest.mark.pagination
@pytest.mark.parametrize("ddt",
                         deal_data.pagination['signature']
                         )
def test_pagination(ddt):
    resp = lib.get_deal_by_user_id(page=ddt['data']['page'],
                                   size=ddt['data']['size'])
    result = lib.json_similarity(ddt['expected'], resp.json(), verbose=False)
    assert result is True