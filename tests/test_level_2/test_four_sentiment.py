import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__equal_good_words_num_bad_words_num():
    text = "Ехал Грека через реку. Видит Грека: в реке рак. Сунул в реку руку Грека. Рак за руку Греку — цап."
    good_words = {"грека", "ехал"}
    bad_words = {"рак", "сунул"}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check is None


def test__check_tweet_sentiment__not_good_words_num_and_not_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {}
    bad_words = {}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check is None


def test__check_tweet_sentiment__one_good_words_num_and_not_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {"грека"}
    bad_words = {}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check == "GOOD"

  
def test__check_tweet_sentiment__not_good_words_num_and_one_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {}
    bad_words = {"грека"}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check == "BAD"


def test__check_tweet_sentiment__repeat_good_words_num():
    text = "Ехал Грека через реку"
    good_words = {"грека","грека"}
    bad_words = {"ехал"}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check is None

   
def test__check_tweet_sentiment__empty_text():
    text = ""
    good_words = {"грека","грека"}
    bad_words = {"ехал"}

    check = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert check is None


@pytest.mark.parametrize(
    "text, good_words, bad_words, result",
    [
        ("Ехал Грека через реку. Видит Грека: в реке рак. Сунул в реку руку Грека. Рак за руку Греку — цап.",
         {"грека", "ехал"}, {"рак", "сунул"}, None),
        ("Ехал Грека через реку", {}, {}, None),
        ("Ехал Грека через реку", {"грека","грека"}, {"ехал"}, None),
        ("", {"грека","грека"}, {"ехал"}, None)
    ]
)
def test__check_tweet_sentiment__(text, good_words, bad_words, result):
    assert check_tweet_sentiment(text, good_words, bad_words) is result


@pytest.mark.parametrize(
    "text, good_words, bad_words, result",
    [
        ("Ехал Грека через реку", {"грека"}, {}, "GOOD"),
        ("Ехал Грека через реку", {}, {"грека"}, "BAD")
    ]
)
def test__check_tweet_sentiment__two(text, good_words, bad_words, result):
    assert check_tweet_sentiment(text, good_words, bad_words) == result