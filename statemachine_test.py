#let it be so
import pytest
from deepdiff import DeepDiff

import statemachine_data
from lib import post_deal, update_deal, get_deal_by_deal_id, post_event, post_application, su_status
from statemachine_data import available_envs, envs, ddt_set


@pytest.mark.statemachine
@pytest.mark.parametrize("environment", envs)
@pytest.mark.parametrize("test", ddt_set)
def test_events_post(environment, test):
    if environment not in available_envs[test['state']]:
        pytest.skip(str(environment) + " is not possible Env for state " + str(test['state']))
    deal_id, application_id = su_status(test['state'], environment)
    transition_result = post_event(deal_id, test['event'])
    assert transition_result.json()['success'] is test['result']


@pytest.mark.isReturnedToMiddle
def test_102_is_return_to_middle_trigger_set_up_false():
    deal_id, application_id = su_status('102', 's-101')
    resp = get_deal_by_deal_id(deal_id=deal_id)
    assert resp.json()['data'][0]['isReturnedToMiddle'] is False


@pytest.mark.isReturnedToMiddle
def test_102_is_return_to_middle_trigger_switch_to_on():
    deal_id, application_id = su_status('102', 's-101')
    post_event(deal_id, "CREDIT_RETURNED_MIDDLE")
    resp = get_deal_by_deal_id(deal_id=deal_id)
    assert resp.json()['data'][0]['isReturnedToMiddle'] is True


@pytest.mark.isReturnedToMiddle
def test_104_is_return_to_middle_trigger_set_up_false():
    deal_id, application_id = su_status('104', 's-104')
    resp = get_deal_by_deal_id(deal_id=deal_id)
    assert resp.json()['data'][0]['isReturnedToMiddle'] is False


@pytest.mark.isReturnedToMiddle
def test_104_is_return_to_middle_trigger_switch_to_on():
    deal_id, application_id = su_status('104', 's-104')
    post_event(deal_id, "CREDIT_RETURNED_MIDDLE")
    resp = get_deal_by_deal_id(deal_id=deal_id)
    assert resp.json()['data'][0]['isReturnedToMiddle'] is True


@pytest.mark.application
@pytest.mark.parametrize("ddt", statemachine_data.application['phone_validation'])
def test_phone_validation(ddt):
    result = False
    resp = post_application(deal_id="", j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_post_validation']['channelId']
                         )
def test_deal_dictionary_fields_post(ddt):
    result = False
    resp = post_deal(j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_put_validation']['channelId']
                         )
def test_deal_dictionary_fields_put(ddt):
    result = False
    resp = post_deal(j=ddt['precondition'])
    resp = update_deal(deal_id=resp.json()['data'][0]['id'], j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_post_validation']['calcId']
                         )
def test_deal_calc_id_post(ddt):
    result = False
    resp = post_deal(j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_put_validation']['calcId']
                         )
def test_deal_calc_id_put(ddt):
    result = False
    resp = post_deal(j=ddt['precondition'])
    resp = update_deal(deal_id=resp.json()['data'][0]['id'], j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


@pytest.mark.events
@pytest.mark.parametrize("ddt",
                         statemachine_data.events['events_fields_post_validation']['rejectionReasonId']
                         )
def test_events_fields_post(ddt):
    result = False
    resp = post_deal()
    resp = post_event(deal_id=resp.json()['data'][0]['id'], j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


# TODO: пофиксить тесты, они смотрят не в ту ручку
@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_post_validation']['paymentMethodId']
                         )
def test_deal_payment_method_id_post(ddt):
    result = False
    resp = post_deal(j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True


# TODO: пофиксить тесты, они смотрят не в ту ручку
@pytest.mark.deal
@pytest.mark.parametrize("ddt",
                         statemachine_data.deal['deal_fields_put_validation']['paymentMethodId']
                         )
def test_deal_payment_method_id_put(ddt):
    result = False
    resp = post_deal(j=ddt['precondition'])
    resp = update_deal(deal_id=resp.json()['data'][0]['id'], j=ddt['data'])
    df = DeepDiff(ddt['expected'], resp.json())
    if not ('dictionary_item_removed' in df.keys() or 'values_changed' in df.keys()):
        result = True
    assert result is True
