import documents_data
import lib
import pytest


def generate_test_result(j, deal_id, file_id=None):
    result = j
    if result['success']:
        result['data'][0]['dealId'] = deal_id
        if file_id:
            result['data'][0]['fileId'] = file_id
    return result


@pytest.mark.skipif(True, reason='уже сделано, отлаживаем остальные')
@pytest.mark.documents
@pytest.mark.parametrize("ddt",
                         documents_data.post['required']
                         )
def test_documents_post(ddt):
    if 'precondition' in ddt.keys():
        if 'post_doc_to_deal' in ddt['precondition'].keys():
            if ddt['precondition']['post_doc_to_deal'].keys():
                prec_deal_id, prec_application_id = lib.su_status('100', 's-0')
                prec_file_id = lib.post_ducument_into_filestorage().json()["data"]['id']
                lib.post_document_into_deal(deal_id=prec_deal_id,
                                            file_id=prec_file_id,
                                            j=ddt['precondition']['post_doc_to_deal'])
                ddt["data"]['fileId'] = prec_file_id
    if 'fileId' in ddt["data"].keys():
        file_id = ddt["data"]['fileId']
        ddt['data'].pop('fileId')
    else:
        file_id = lib.post_ducument_into_filestorage().json()["data"]['id']
    if 'dealId' in ddt["data"].keys():
        deal_id = ddt["data"]['dealId']
        ddt['data'].pop('dealId')
    else:
        deal_id, application_id = lib.su_status('100', 's-0')
    resp = lib.post_document_into_deal(deal_id=deal_id,
                                       file_id=file_id,
                                       j=ddt['data'])
    expected = generate_test_result(j=ddt['expected'], deal_id=deal_id, file_id=file_id)
    result = lib.json_include(expected, resp.json(), verbose=False)
    assert result is True


@pytest.mark.documents
@pytest.mark.parametrize("ddt",
                         documents_data.delete
                         )
def test_documents_delete(ddt):
    if 'post_doc_to_deal' in ddt['precondition']:
        deal_id, prec_application_id = lib.su_status('100', 's-0')
        file_id = lib.post_ducument_into_filestorage().json()["data"]['id']
        doc_id = lib.post_document_into_deal(deal_id=deal_id,
                                             file_id=file_id,
                                             j=ddt['precondition']['post_doc_to_deal']
                                             ).json()['data'][0]['id']
    elif 'data' in ddt['precondition']:
        doc_id = ddt['precondition']['data']['id']
    else:
        raise Exception('Не может быть получен ID документа')
    if ddt['precondition']['delete_deal']:
        lib.delete_document(doc_id)
    resp = lib.delete_document(doc_id)
    if 'json' in ddt['expected'].keys():
        result = lib.json_include(ddt['expected']['json'], resp.json(), verbose=False)
    elif 'sql' in ddt['expected'].keys():
        sql_request = ddt['expected']['sql']['request'] % str(deal_id)
        result = ddt['expected']['sql']['result'] == lib.make_sql_request(sql_request)
    else:
        raise Exception('Не указан тип ожидаемого результата')
    assert result is True

