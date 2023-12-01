from functions.level_1.two_date_parser import compose_datetime_from
import datetime

def test__compose_datetime_from__empty_date_str():
    assert compose_datetime_from(
        date_str='',
        time_str=datetime.datetime.now().time().strftime("%H:%M")
        ) == datetime.datetime.strptime(
            datetime.datetime.now().strftime("%y-%m-%d %H:%M"),
            "%y-%m-%d %H:%M")

def test__compose_datetime_from__date_str_is_tomorrow():
    assert compose_datetime_from(
        date_str="tomorrow",
        time_str=datetime.datetime.now().time().strftime("%H:%M")
        ) == datetime.datetime.strptime(
            datetime.datetime.now().strftime("%y-%m-%d %H:%M"),
            "%y-%m-%d %H:%M") + datetime.timedelta(days=1)
