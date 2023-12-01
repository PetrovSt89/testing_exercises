import pytest

from functions.level_2.three_first import first

def test__first__two_items():
    assert first(items=[1,2]) == 1


def test__first__one_item():
    assert first(items=[5]) == 5


def test__first__empty_dict_with_default():
    assert first(items=[], default=0) == 0

    
def test__first__empty_dict_not_default():
    with pytest.raises(AttributeError):
        first(items=[]) 

