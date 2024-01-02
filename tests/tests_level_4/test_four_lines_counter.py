from functions.level_4.four_lines_counter import count_lines_in


def test__count_lines_in__empty(empty_filepath_fix):
    assert count_lines_in(empty_filepath_fix) == 0


def test__count_lines_in__no_file():
    assert count_lines_in(filepath='none.txt') is None


def test__count_lines_in__three_lines(filepath_fix):
    assert count_lines_in(filepath=filepath_fix) == 3


def test__count_lines_in__with_comment(filepath_with_comment_fix):
    assert count_lines_in(filepath=filepath_with_comment_fix) == 2