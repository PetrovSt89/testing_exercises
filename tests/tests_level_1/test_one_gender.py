from functions.level_1.one_gender import genderalize


def test__genderalize__gender_is_male():
    assert genderalize('муж', 'жен', 'male') == 'муж'

def test__genderalize__no_gender():
    assert genderalize('муж', 'жен', '') == 'жен'
