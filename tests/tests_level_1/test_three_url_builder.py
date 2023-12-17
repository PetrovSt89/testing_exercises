import pytest
from functions.level_1.three_url_builder import build_url
from typing import Mapping


def test__build_url__None_get_params():
    assert build_url(
        'http://127.0.0.1:5000',
        'xrenznaet',
        None) == 'http://127.0.0.1:5000/xrenznaet'

def test__build_url__one_get_params():
    assert build_url(
        'http://127.0.0.1:5000',
        'xrenznaet',
        {'lang':'ru'}) == 'http://127.0.0.1:5000/xrenznaet?lang=ru'


def test__build_url__two_get_params():
    assert build_url(
        'http://127.0.0.1:5000',
        'xrenznaet',
        {'page':'2','lang':'ru'}) == 'http://127.0.0.1:5000/xrenznaet?page=2&lang=ru'
    

def test__build_url__two_params():
    assert build_url('xrenznaet',
        {'page':'2','lang':'ru'}) == "xrenznaet/{'page': '2', 'lang': 'ru'}"


def test__build_url__no_host_name():
    with pytest.raises(TypeError):
        build_url(relative_url='xrenznaet',
                    get_params={'page':'2','lang':'ru'})
        

def test__build_url__no_params():
    with pytest.raises(TypeError):
        build_url()


@pytest.mark.parametrize(
    "host_name, relative_url, get_params, result",
    [
        ('http://127.0.0.1:5000', 'xrenznaet', None, 'http://127.0.0.1:5000/xrenznaet'),
        ('http://127.0.0.1:5000', 'xrenznaet', {'lang':'ru'}, 'http://127.0.0.1:5000/xrenznaet?lang=ru'),
        ('http://127.0.0.1:5000', 'xrenznaet', {'page':'2','lang':'ru'},
        'http://127.0.0.1:5000/xrenznaet?page=2&lang=ru'),
        ('http://127.0.0.1:5000','xrenznaet', {'page':'2','lang':'ru'}, "http://127.0.0.1:5000/xrenznaet?page=2&lang=ru"),
    ]
)
def test__build_url__(host_name, relative_url, get_params, result):
    assert build_url(host_name, relative_url, get_params) == result