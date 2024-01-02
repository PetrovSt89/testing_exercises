import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes






@pytest.mark.parametrize(
    "name, result",
    [
        ('{}', ''),
        ('{}', ''),
        ('{stas}', 'ta'),
        ('{{stas}}', 'stas')
    ]
)
def test__delete_remove_brackets_quotes(name, result):
    assert delete_remove_brackets_quotes(name) == result
