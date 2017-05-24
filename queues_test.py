import lib
import queues_data
import pytest
import lib
import uuid
import time
import json

vhost = "%2fdeal_stage"
queue = "testQueue"


def generate_test_result(deal_id, current_status_id, event, modified_by=1, borrower_cas_id=None):
    result = {
        'properties': {
            'headers': {
                '__TypeId__': 'DEAL_STATUS_TRANSITION'
            }
        },
        'payload': {
            'dealId': deal_id,
            'borrowerCasId': borrower_cas_id,
            'event': event,
            'currentStatusId': current_status_id,
            'modifiedBy': modified_by
        }
    }
    return result


@pytest.mark.queue
@pytest.mark.parametrize("ddt", queues_data.avalible_transitions)
def test_statemachine_transitions_messaging(ddt):
    deal_id, application_id = lib.su_status(ddt['state'], 's-202')
    correlation_id = str(uuid.uuid4())
    lib.purge_queue(vhost=vhost, queue=queue)
    lib.post_event(deal_id=deal_id, event=ddt['event'], corellation_id=correlation_id)
    message = lib.get_message_by_corellation_id(
                  raw_json=lib.get_message_from_queue(vhost=vhost, queue=queue).json(),
                  corellation_id=correlation_id
    )
    time.sleep(1)
    if not message:
        result = False
    else:
        message["payload"] = json.loads(message["payload"])
        expected = generate_test_result(deal_id=deal_id,
                                        current_status_id=lib.status_num_to_id_converter(ddt['transition']),
                                        event=ddt['event']
                                        )
        result = lib.json_include(json_expected=expected,
                                  json_actual=message,
                                  verbose=False)
    assert result is ddt['result']

# Нужно написать ещё тесты на:
    # неотправку события на кривые преходы