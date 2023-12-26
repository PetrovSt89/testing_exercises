import pytest
from functions.level_1.one_gender import genderalize


def test__genderalize__gender_is_male(gender_fix):
    assert genderalize(verb_male=gender_fix.male, verb_female=gender_fix.female, gender='male') == gender_fix.male

def test__genderalize__no_gender(gender_fix):
    assert genderalize(verb_male=gender_fix.male, verb_female=gender_fix.female, gender='') == gender_fix.female


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, result",
    [
        ('муж', 'жен', 'male', 'муж'),
        ('муж', 'жен', '', 'жен')
    ]
)
def test__genderalize__(verb_male, verb_female, gender, result):
    assert genderalize(verb_male, verb_female, gender) == result