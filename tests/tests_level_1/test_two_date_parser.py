import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from


datetime_now = datetime.datetime.now()
str_datetime_now = datetime_now.strftime("%y-%m-%d %H:%M")

def test__compose_datetime_from__empty_date_str():
    assert compose_datetime_from(
        date_str='',
        time_str=datetime_now.time().strftime("%H:%M")
        ) == datetime.datetime.strptime(str_datetime_now, "%y-%m-%d %H:%M")

def test__compose_datetime_from__date_str_is_tomorrow():
    assert compose_datetime_from(
        date_str="tomorrow",
        time_str=datetime_now.time().strftime("%H:%M")
        ) == datetime.datetime.strptime(
            str_datetime_now, "%y-%m-%d %H:%M"
            ) + datetime.timedelta(days=1)


@pytest.mark.parametrize(
    "date_str, time_str, result",
    [
        ('', datetime_now.time().strftime("%H:%M"), 
            datetime.datetime.strptime(str_datetime_now, "%y-%m-%d %H:%M")),
        ("tomorrow", datetime_now.time().strftime("%H:%M"), 
            datetime.datetime.strptime(
        str_datetime_now, "%y-%m-%d %H:%M"
        ) + datetime.timedelta(days=1))
    ]
)
def test__compose_datetime_from__(date_str, time_str, result):
    assert compose_datetime_from(date_str, time_str) == result
