import pytest
from functions.level_4.two_students import get_student_by_tg_nickname


def test__get_student_by_tg_nickname__empty():
    assert get_student_by_tg_nickname(telegram_username='', students=[]) is None


def test__get_student_by_tg_nickname__empty_list():
    assert get_student_by_tg_nickname(telegram_username='stas', students=[]) is None


def test__get_student_by_tg_nickname__one_student_no_username(student_stas_fix):
    assert get_student_by_tg_nickname(
        telegram_username='', students=[student_stas_fix]
        ) is None


def test__get_student_by_tg_nickname__no_account(student_vasia_fix):
    assert get_student_by_tg_nickname(
        telegram_username='vasia', students=[student_vasia_fix]
        ) is None


def test__get_student_by_tg_nickname__one_student_with_account(student_stas_fix):
    assert get_student_by_tg_nickname(
        telegram_username='stas', students=[student_stas_fix]
        ) == student_stas_fix


def test__get_student_by_tg_nickname__two_students(list_students, student_dasha_fix):
    assert get_student_by_tg_nickname(
        telegram_username='dasha', students=list_students
        ) == student_dasha_fix


