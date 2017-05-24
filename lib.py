import json

import requests
from deepdiff import DeepDiff
import psycopg2

service_domain_name = ''
queue_domain_name = ''

db_setup = {
    'db_name': '',
    'db_port': ,
    'db_user': '',
    'ssh_user': '',
    'ssh_port': ,
    'key': '',
    'pass': ''
}

status_mapa = {
    '100': {'start': True, 'env': 's-0'},
    '003': {'start': False, 'from': '100', 'event': 'DEAL_CANCELLED_BY_CUSTOMER', 'env': 's-0'},
    '004': {'start': False, 'from': '100', 'event': 'BORROWER_APPROVAL_EXPIRED', 'env': 's-0'},
    '106': {'start': False, 'from': '100', 'event': 'CREDIT_SENT_INTERNET', 'env': 's-0'},
    '107': {'start': False, 'from': '106', 'event': 'CREDIT_ACCEPTED_MIDDLE', 'env': 's-0'},
    '108': {'start': False, 'from': '107', 'event': 'CREDIT_RETURNED_CLIENT', 'env': 's-0'},
    '101': {'start': False, 'from': '100', 'event': 'CREDIT_SENT', 'env': 's-101'},
    '102': {'start': False, 'from': '101', 'event': 'CREDIT_ACCEPTED', 'env': 's-101'},
    '001': {'start': False, 'from': '102', 'event': 'NOT_CREDIT_PRODUCT', 'env': 's-101'},
    '103': {'start': False, 'from': '102', 'event': 'CREDIT_RETURNED', 'env': 's-101'},
    '104': {'start': False, 'from': '102', 'event': 'CREDIT_ANALYZE', 'env': 's-104'},
    '002': {'start': False, 'from': '104', 'event': 'CREDIT_REJECTED', 'env': 's-104'},
    '105': {'start': False, 'from': '104', 'event': 'CREDIT_APPROVED', 'env': 's-104'},
    '201': {'start': False, 'from': '105', 'event': 'DEAL_CREATED', 'env': 's-201'},
    '202': {'start': False, 'from': '201', 'event': 'BORROWER_APPROVED', 'env': 's-202'},
    '301': {'start': False, 'from': '202', 'event': 'AGENCY_SELECTED', 'env': 's-202'},
    '203': {'start': False, 'from': '202', 'event': 'ESTATE_DOCUMENTS_SENT', 'env': 's-202'},
    '302': {'start': False, 'from': '203', 'event': 'ESTATE_DOCUMENTS_RETURNED_FROM_AGENT', 'env': 's-202'},
    '204': {'start': False, 'from': '202', 'event': 'CLIENT_ALREADY_HAS_ESTATE', 'env': 's-202'},
    '401': {'start': False, 'from': '204', 'event': 'ESTATE_APPROVED_PRIMARY', 'env': 's-202'},
    '402': {'start': False, 'from': '204', 'event': 'ESTATE_APPROVED_RESALE', 'env': 's-202'},
    '005': {'start': False, 'from': '402', 'event': 'ESTATE_BOUGHT_NOTIFICATION', 'env': 's-202'},
}
env_list = {
    's-0': {
        'application': {},
        'deal': {}
    },
    's-101': {
        'application': {
            "personFirstName": "Vasya",
            "personLastName": "Pupkin",
            "personBirthday": "1953-04-04TZ",
            "contactPhoneMobile": "1987654321",
            "passportSeries": "1234",
            "passportNumber": "567890",
            "applicationTypePledger": False,
            "mandatoryCoBorrower": False,
            "applicationStatus": "DRAFT",
            "considerCoBorrowerIncome": False,
            "applicationType": "BORROWER"
        },
        'deal': {
            "sumSupposes": 1000000,
            "productTypeId": 15020,
            "officeId": 666,
            "requestedSum": 6666666,
        }
    },
    's-104': {
        'application': {
            "personFirstName": "Vasya",
            "personLastName": "Pupkin",
            "personBirthday": "1953-04-04TZ",
            "contactPhoneMobile": "1987654321",
            "passportSeries": "1234",
            "passportNumber": "567890",
            "applicationTypePledger": False,
            "mandatoryCoBorrower": False,
            "applicationStatus": "DRAFT",
            "considerCoBorrowerIncome": False,
            "applicationType": "BORROWER"
        },
        'deal': {
            "sumSupposes": 1000000,
            "creditAnalysisId": 11010,
            "transactId": 666666,
            "productTypeId": 15020,
            "officeId": 666,
            "requestedSum": 6666666,
        }
    },
    's-107': {
        'application': {
            "personFirstName": "Василий",
            "personLastName": "Пупкин",
            "personMiddleName": "Владимирович",
            "personBirthday": "1953-04-04TZ",
            "contactPhoneMobile": "1987654321",
            "passportSeries": "1234",
            "passportNumber": "567890",
            "applicationTypePledger": False,
            "mandatoryCoBorrower": False,
            "applicationStatus": "DRAFT",
            "considerCoBorrowerIncome": False,
            "applicationType": "BORROWER"
        },
        'deal': {
            "sumSupposes": 1000000,
            "productTypeId": 15110,
            "subproductTypeId": 16010,
            "objectTypeId": 9020,
            "officeId": 5,
            "requestedSum": 6666666,
        }
    },
    's-201': {
        'application': {
            "personFirstName": "Vasya",
            "personLastName": "Pupkin",
            "personBirthday": "1953-04-04TZ",
            "contactPhoneMobile": "1987654321",
            "passportSeries": "1234",
            "passportNumber": "567890",
            "applicationTypePledger": False,
            "mandatoryCoBorrower": False,
            "applicationStatus": "DRAFT",
            "considerCoBorrowerIncome": False,
            "applicationType": "BORROWER"
        },
        'deal': {
            "sumSupposes": 1000000,
            "creditAnalysisId": 11010,
            "transactId": 666666,
            "subproductTypeId": 16050,
            "productTypeId": 15020,
            "officeId": 666,
            "requestedSum": 6666666,
            "channelId": 12030,
            "loanPeriod": 66,
        }
    },
    's-202': {
        'application': {
            "personFirstName": "Vasya",
            "personLastName": "Pupkin",
            "personBirthday": "1953-04-04TZ",
            "contactPhoneMobile": "1987654321",
            "passportSeries": "1234",
            "passportNumber": "567890",
            "applicationTypePledger": False,
            "mandatoryCoBorrower": False,
            "applicationStatus": "DRAFT",
            "considerCoBorrowerIncome": False,
            "applicationType": "BORROWER"
        },
        'deal': {
            "sumSupposes": 1000000,
            "interestRate": 66.6,
            "creditAnalysisId": 11010,
            "transactId": 666666,
            "subproductTypeId": 16050,
            "productTypeId": 15020,
            "officeId": 666,
            "requestedSum": 6666666,
            "channelId": 12030,
            "loanPeriod": 66,
            "approvedSum": 7777777,
            "firstApprovedDate": "2953-04-04T01:17:54.731Z",

        }
    },
}
status_ids = {
    '100': 8060,
    '101': 8070,
    '102': 8080,
    '103': 8090,
    '104': 8100,
    '105': 8110,
    '106': 8200,
    '107': 8210,
    '108': 8220,
    '201': 8120,
    '202': 8130,
    '203': 8140,
    '204': 8150,
    '301': 8160,
    '302': 8170,
    '401': 8180,
    '402': 8190,
    '001': 8010,
    '002': 8020,
    '003': 8030,
    '004': 8040,
    '005': 8050,
}


def make_sql_request(sql_request, db_setup=db_setup):
    db_conn_str = "dbname='" + str(db_setup['db_name']) + \
                  "' user='" + str(db_setup['db_user']) + \
                  "' host='localhost' port='" + str(db_setup['db_port']) + \
                  "' password='" + str(db_setup['pass']) + "'"
    try:
        conn = psycopg2.connect(db_conn_str)
        cur = conn.cursor()
        cur.execute(sql_request)
        result = cur.fetchall()
        cur.close()
    except:
        result = 'При выполнении запроса что-то пошло не так'
    return result


def json_include(json_expected, json_actual, verbose=False):
    df = DeepDiff(json_expected, json_actual)
    if verbose:
        print(json_expected)
        print()
        print(json_actual)
        print()
        print(df)
    return not ('dictionary_item_removed' in df.keys() or
                'values_changed' in df.keys() or
                'iterable_item_removed' in df.keys())


# TODO: тут нужно будет уточнить, что формат должен полностью совпадать.
# TODO: Для этого в идеале валидироваться по JSON Schema
def json_similarity(json_expected, json_actual, verbose=False):
    df = DeepDiff(json_expected, json_actual)
    if verbose:
        print(json_expected)
        print()
        print(json_actual)
        print()
        print(df)
    return not ('dictionary_item_removed' in df.keys() or
                'iterable_item_removed' in df.keys()
                )


def post_deal(j=None):
    r_url = service_domain_name + '/api/v1/deals'
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    r_json = {"authorId": 1}
    if j:
        r_json.update(j)
    r_json = json.dumps(r_json)
    r = requests.post(url=r_url,
                      data=r_json,
                      headers=r_headers)
    return r


def update_deal(deal_id, j):
    deal_id = str(deal_id)
    r_url = service_domain_name + '/api/v1/deals/' + deal_id
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    i_json = {'authorId': 1}
    i_json.update(j)
    i_json.update({'id': deal_id})
    r_json = json.dumps(i_json)
    r = requests.put(url=r_url,
                     data=r_json,
                     headers=r_headers)
    return r


def delete_deal(deal_id, verbose=False):
    deal_id = str(deal_id)
    r_url = service_domain_name + '/api/v1/deals/' + deal_id
    r_headers = {"Accept": "application/json", 'X-Cas-Id': '1'}
    r = requests.delete(url=r_url,
                        headers=r_headers)
    if verbose:
        print(r_url)
        print(r, r.text)
    return r


def get_deal_by_deal_id(deal_id):
    deal_id = str(deal_id)
    r_url = service_domain_name + '/api/v1/deals/' + deal_id
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    r = requests.get(url=r_url,
                     headers=r_headers)
    return r


def get_deal_by_user_id(user_id=None, page=None, size=None):
    r_url = service_domain_name + '/api/v1/deals/?'
    if user_id:
        r_url += '&userId=' + str(user_id)
    if page:
        r_url += '&page=' + str(page)
    if size:
        r_url += '&size=' + str(size)
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    r = requests.get(url=r_url,
                     headers=r_headers)
    return r


def post_event(deal_id, event=None, j=None, corellation_id=None):
    r_url = service_domain_name + '/api/v1/events'
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    if corellation_id:
        r_headers.update({'Correlation-Id': corellation_id})
    if event:
        r_json = '{"event": "%s", "id": %s, "userId": 1}' % (str(event), str(deal_id))
    elif j:
        r_json = {'userId': 1}
        r_json.update(j)
        r_json.update({'id': deal_id})
        r_json = json.dumps(r_json)
    else:
        raise Exception('Не указаны ключ словаря состояний или полный JSON для выполнения')

    r = requests.post(url=r_url,
                      data=r_json,
                      headers=r_headers)

    return r


def post_application(deal_id, j):
    r_url = service_domain_name + '/api/v1/applications'
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    i_json = {}
    i_json.update(j)
    if deal_id is not None:
        i_json.update({'dealId': deal_id})
    r_json = json.dumps(i_json)
    r = requests.post(url=r_url,
                      data=r_json,
                      headers=r_headers)
    return r


def delete_application(application_id):
    application_id = str(application_id)
    r_url = service_domain_name + '/api/v1/applications/' + application_id
    r_headers = {"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"}
    r = requests.delete(url=r_url,
                        headers=r_headers)
    return r


def generate_path(status):
    if status_mapa[status]['start']:
        result = [status]
    else:
        result = generate_path(status_mapa[status]['from']) + [status]

    return result


def generate_env(env, deal_id):
    deal_id = update_deal(deal_id, env_list[env]['deal']).json()['data'][0]['id']
    application_id = post_application(deal_id, env_list[env]['application']).json()['data'][0]['id']

    return deal_id, application_id


def su_status(status, env):
    path = generate_path(status)
    deal_id = post_deal().json()['data'][0]['id']
    # TODO: return selection of env
    if env != 's-0':
        deal_id, application_id = generate_env(env, deal_id)
    else:
        application_id = None
    for s in path[1:]:
        post_event(deal_id, status_mapa[s]['event'])

    return deal_id, application_id


def purge_queue(vhost, queue):
    r_url = queue_domain_name + '/api/queues/' + vhost + '/' + queue + '/contents'
    r_headers = {
        'authorization': "Basic cG9ydGFsX3JtcTowbnVQVm5UbXJudTludndjbXlBNw==",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        'origin': "https://strmq.parline.ru",
        'content-type': "text/plain;charset=UTF-8",
        'referer': "https://strmq.parline.ru/",
    }
    r = requests.request(method="DELETE", url=r_url, headers=r_headers)
    return r


def get_message_from_queue(vhost, queue):
    r_url = queue_domain_name + '/api/queues/' + vhost + '/' + queue + '/get'
    r_headers = {
        'authorization': "Basic cG9ydGFsX3JtcTowbnVQVm5UbXJudTludndjbXlBNw==",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        'origin': "https://strmq.parline.ru",
        'content-type': "text/plain;charset=UTF-8",
        'referer': "https://strmq.parline.ru/",
    }
    r_body = {"count": 50,
              "requeue": True,
              "encoding": "auto"}
    r_body = json.dumps(r_body)
    r = requests.request(method="POST", url=r_url, headers=r_headers, data=r_body)
    return r


def get_message_by_corellation_id(raw_json, corellation_id):
    result = None
    for item in raw_json:
        if item['properties']['headers']['__CorrelationId__'] == corellation_id:
            result = item
    return result


def status_num_to_id_converter(num):
    return status_ids[num]


def post_ducument_into_filestorage(verbose=False):
    url = "https://qa.domclick.ru/fs/srv/v1/files/"
    query = '?permission=PUBLIC'
    headers = {
        'authorization': "Basic YXBpOnBhc3M=",
        }
    files = {'file': ('deadpool.jpg', open('deadpool.jpg', 'rb'), 'image/jpg', {'permission': 'public'})}
    r = requests.request("POST", url+query, files=files, headers=headers)
    if verbose:
        print(r.text)
    return r


def post_document_into_deal(deal_id, file_id, j):
    r_url = service_domain_name + '/api/v1/documents'
    r_headers = {"Accept": "application/json", "X-Cas-Id": "2", "Content-Type": "application/json"}
    r_json = ({'dealId': deal_id})
    r_json.update({'fileId': file_id})
    if j:
        r_json.update(j)
    r_json = json.dumps(r_json)
    r = requests.post(url=r_url,
                      data=r_json,
                      headers=r_headers)
    return r


def delete_document(doc_id):
    r_url = service_domain_name + '/api/v1/documents/' + str(doc_id)
    r_headers = {"Accept": "application/json", "X-Cas-Id": "2", "Content-Type": "application/json"}
    r = requests.delete(url=r_url,
                        headers=r_headers)
    return r