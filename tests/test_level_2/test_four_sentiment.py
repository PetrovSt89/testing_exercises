from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__equal_good_words_num_bad_words_num():
    text = "Ехал Грека через реку. Видит Грека: в реке рак. Сунул в реку руку Грека. Рак за руку Греку — цап."
    good_words = {"грека", "ехал"}
    bad_words = {"рак", "сунул"}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == None


def test__check_tweet_sentiment__not_good_words_num_and_not_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {}
    bad_words = {}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == None


def test__check_tweet_sentiment__one_good_words_num_and_not_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {"грека"}
    bad_words = {}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == "GOOD"

  
def test__check_tweet_sentiment__not_good_words_num_and_one_bad_words_num():
    text = "Ехал Грека через реку"
    good_words = {}
    bad_words = {"грека"}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == "BAD"


def test__check_tweet_sentiment__repeat_good_words_num():
    text = "Ехал Грека через реку"
    good_words = {"грека","грека"}
    bad_words = {"ехал"}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == None

   
def test__check_tweet_sentiment__empty_text():
    text = ""
    good_words = {"грека","грека"}
    bad_words = {"ехал"}

    func = check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)

    assert func == None
