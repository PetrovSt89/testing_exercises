import pytest
from functions.level_2.one_median import get_median_value


def test__get_median_value__empty_items():
    assert get_median_value(items=[]) == None

#проверка нечетного списка, когда все значения разные
def test__get_median_value__odd_items():
    assert get_median_value(items=[5, 3, 4, 2, 1]) == 3

#проверка нечетного списка, когда есть одинаковые значения
def test__get_median_value__odd_repeat_items():
    assert get_median_value(items=[11, 9, 3, 5, 5]) == 5

#проверка четного списка
def test__get_median_value__even_items():
    assert get_median_value(items=[7, 1, 5, 3]) == 4


def test__get_median_value__two_items():
    assert get_median_value(items=[2, 1]) == 1


def test__get_median_value__one_item():
    assert get_median_value(items=[7]) == 7


@pytest.mark.parametrize(
    "items, result",
    [
        ([], None),
        ([5, 3, 4, 2, 1], 3),
        ([11, 9, 3, 5, 5], 5),
        ([7, 1, 5, 3], 4),
        ([2, 1], 1),
        ([7], 7)
    ]
)
def test__get_median_value__(items, result):
    assert get_median_value(items) == result