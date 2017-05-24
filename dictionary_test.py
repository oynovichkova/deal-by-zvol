import requests
import pytest
import lib
from dictionary_data import dictionary


def dictionary_get(dictionary_type, dependent_by_id=None, **headers):
    r_url = lib.service_domain_name + '/api/v1/dictionaries/' + str(dictionary_type)
    if dependent_by_id:
        r_url += "?dependentById=" + str(dependent_by_id)
    r_headers = headers if headers else {}
    r_headers.update({"Accept": "application/json", "cas_id": "1", "Content-Type": "application/json"})
    r = requests.get(url=r_url,
                     headers=r_headers)
    return r


@pytest.mark.dictionary
@pytest.mark.parametrize("ddt",
                         dictionary['get_validation']['dictionary_tests']
                         )
def test_dictionary_get(ddt):
    """
    В тесте смотрим чтобы соблюдалось наличие полей (т.е. чтобы не были добавлены новые.
    TODO: Нужно будет перевести валидацию на JSON Schema, когда Илья мне отдаст их
    Также смотрим, что по указанному типу словаря мы получаем именно те данные, которые нам нужны.
    TODO: Выделить получение нужной информации в отдельный тест, с положением в базу словаря из одной записи.
        Так будет проще.
    """
    resp = dictionary_get(dictionary_type=ddt['data']['dictionary_type'])
    result = lib.json_similarity(ddt['expected'], resp.json())
    if resp.json()['success']:
        for i in ddt['expected']['dictionaries'][ddt['data']['dictionary_type']]:
            result_for_i = False
            for k in resp.json()['dictionaries'][ddt['data']['dictionary_type']]:
                result_for_i |= lib.json_include(i, k, verbose=False)
            result &= result_for_i
    assert result is True


@pytest.mark.dictionary
@pytest.mark.parametrize("ddt",
                         dictionary['get_validation']['subset_tests']
                         )
def test_dictionary_subset(ddt):
    """
    В тесте смотрим чтобы соблюдалось наличие полей (т.е. чтобы не были добавлены новые.
    TODO: Нужно будет перевести валидацию на JSON Schema, когда Илья мне отдаст их
    Также смотрим, что по указанному типу словаря и фильтру связанного словаря
        мы получаем именно те данные, которые нам нужны.
    TODO: Выделить получение нужной информации в отдельный тест, с положением в базу словаря из одной записи.
        Так будет проще.
    """
    resp = dictionary_get(dictionary_type=ddt['data']['dictionary_type'],
                          dependent_by_id=ddt['data']['dependentById']
                          )
    result = lib.json_similarity(ddt['expected'], resp.json())
    if resp.json()['success']:
        for i in ddt['expected']['dictionaries'][ddt['data']['dictionary_type']]:
            result_for_i = False
            for k in resp.json()['dictionaries'][ddt['data']['dictionary_type']]:
                result_for_i |= lib.json_include(i, k, verbose=False)
            result &= result_for_i
    assert result is True