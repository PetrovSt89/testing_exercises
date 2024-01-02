from unittest.mock import patch
from functions.level_4.three_promocodes import generate_promocode


def test__generate_promocode__empty():
    with patch('functions.level_4.three_promocodes.random.choice') as choice_mock:
        choice_mock.return_value = 'Z'

        result = generate_promocode()

        assert result == 'ZZZZZZZZ'


def test__generate_promocode__one_promocode_len():
    with patch('functions.level_4.three_promocodes.random.choice') as choice_mock:
        choice_mock.return_value = 'Z'

        result = generate_promocode(promocode_len=1)

        assert result == 'Z'