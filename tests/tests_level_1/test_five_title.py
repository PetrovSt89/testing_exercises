import pytest
from functions.level_1.five_title import change_copy_item


def test__change_copy_item__not_additional_copy_text_not_max_main_item_title_length():
    assert change_copy_item(
        title="qwerty"*15
        ) == f"Copy of {'qwerty'*15}"


def test__change_copy_item__better_max_main_item_not_max_main_item_title_length():
    assert change_copy_item(
        title="qwerty"*16 + "qwer"
        ) == "qwerty"*16 + "qwer"


def test__change_copy_item__not_additional_copy_text():
    assert change_copy_item(title="q", max_main_item_title_length= 10) == "Copy of q"


def test__change_copy_item__better_max_main_item():
    assert change_copy_item(title="qw", max_main_item_title_length= 10) == "qw"


def test__change_copy_item__int_element_in_brackets():
    assert change_copy_item(title="Copy of before(123)after") == "Copy of (124)"


def test__change_copy_item__str_element_in_brackets():
    assert change_copy_item(title="Copy of before(Stas)after") == "Copy of before(Stas)after (2)"


def test__change_copy_item__only_value_in_brackets():
    assert change_copy_item(title="Copy of (123)") == "Copy of (124)"


def test__change_copy_item__only_brackets():
    assert change_copy_item(title="Copy of ()") == "Copy of () (2)"


@pytest.mark.parametrize(
    "title, result",
    [
        ("qwerty"*15, f"Copy of {'qwerty'*15}"),
        ("qwerty"*16 + "qwer", "qwerty"*16 + "qwer"),
        ("Copy of before(123)after", "Copy of (124)"),
        ("Copy of before(Stas)after", "Copy of before(Stas)after (2)"),
        ("Copy of (123)", "Copy of (124)"),
        ("Copy of ()", "Copy of () (2)")
    ]
)
def test__change_copy_item__(title, result):
    assert change_copy_item(title) == result


@pytest.mark.parametrize(
    "title, max_main_item_title_length, result",
    [
        ("q", 10, "Copy of q"),
        ("qw", 10, "qw")
    ]
)
def test__change_copy_item__two(title, max_main_item_title_length, result):
    assert change_copy_item(title, max_main_item_title_length) == result