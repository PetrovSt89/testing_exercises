import os
import pytest
from typing import NamedTuple


class Student(NamedTuple):
    first_name: str
    last_name: str
    telegram_account: str | None


@pytest.fixture
def student_stas_fix():
    return Student(first_name='Stas', last_name='Petrov', telegram_account='@stas')


@pytest.fixture
def student_vasia_fix():
    return Student(first_name='Vasia', last_name='Petrov', telegram_account=None)


@pytest.fixture
def student_dasha_fix():
    return Student(first_name='Dasha', last_name='Minina', telegram_account='@dasha')


@pytest.fixture
def list_students(student_stas_fix, student_dasha_fix):
    return [student_stas_fix, student_dasha_fix]


@pytest.fixture
def filepath_fix():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file:
        file.writelines(['1\n', '2\n', '3\n'])

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture
def filepath_with_comment_fix():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file:
        file.writelines(['1\n', '  #2\n', '3\n'])

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture
def empty_filepath_fix():
    path_to_file = 'test_file.txt'
    with open(path_to_file, 'w') as file:
        pass

    yield path_to_file

    os.remove(path_to_file)