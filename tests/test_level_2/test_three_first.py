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

def test__first__two_items_with_default():
    assert first(items=[1,2], default=0) == 1


@pytest.mark.parametrize(
    "items, result",
    [
        ([1,2], 1),
        ([5], 5)
    ]
)
def test__first__(items, result):
    assert first(items) == result


@pytest.mark.parametrize(
    "items, default, result",
    [
        ([], 0, 0),
        ([1,2], 0, 1)
    ]
)
def test__first__two(items, default, result):
    assert first(items, default) == result