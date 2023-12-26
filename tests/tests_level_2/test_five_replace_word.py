import pytest
from functions.level_2.five_replace_word import replace_word


def test__replace_word__success_case():
    text = "Красивое лучше чем уродливое Явное лучше чем неявное Простое лучше чем сложное"
    replace_from = "лучше"
    replace_to = "не хуже"

    rep_word = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert rep_word == "Красивое не хуже чем уродливое Явное не хуже чем неявное Простое не хуже чем сложное"


def test__replace_word__not_change():
    text = "Красивое лучше чем уродливое"
    replace_from = "ничего"
    replace_to = "нет"

    rep_word = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert rep_word == "Красивое лучше чем уродливое"


def test__replace_word__empty_text():
    text = ""
    replace_from = "ничего"
    replace_to = "нет"

    rep_word = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert rep_word == ""


def test__replace_word__no_replace_from():
    text = "Красивое лучше чем уродливое"
    replace_from = ""
    replace_to = "нет"

    rep_word = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert rep_word == "Красивое лучше чем уродливое"


def test__replace_word__no_replace_to():
    text = "Красивое лучше чем уродливое"
    replace_from = "лучше"
    replace_to = ""

    rep_word = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert rep_word == "Красивое  чем уродливое"


@pytest.mark.parametrize(
    "text, replace_from, replace_to, result",
    [
        ("Красивое лучше чем уродливое Явное лучше чем неявное Простое лучше чем сложное",
         "лучше", "не хуже",
         "Красивое не хуже чем уродливое Явное не хуже чем неявное Простое не хуже чем сложное"),
        ("Красивое лучше чем уродливое", "ничего", "нет", "Красивое лучше чем уродливое"),
        ("", "ничего", "нет", ""),
        ("Красивое лучше чем уродливое", "", "нет", "Красивое лучше чем уродливое"),
        ("Красивое лучше чем уродливое", "лучше", "", "Красивое  чем уродливое"),
    ]
)
def test__replace_word__no_replace_to(text, replace_from, replace_to, result):
    assert replace_word(text, replace_from, replace_to) == result