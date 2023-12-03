import pytest
from functions.level_1.one_gender import genderalize


def test__genderalize__gender_is_male():
    assert genderalize(verb_male='муж', verb_female='жен', gender='male') == 'муж'

def test__genderalize__no_gender():
    assert genderalize(verb_male='муж', verb_female='жен', gender='') == 'жен'


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, result",
    [
        ('муж', 'жен', 'male', 'муж'),
        ('муж', 'жен', '', 'жен')
    ]
)
def test__genderalize__(verb_male, verb_female, gender, result):
    assert genderalize(verb_male, verb_female, gender) == result