import pytest
import statistics

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__zero_expense():
    with pytest.raises(statistics.StatisticsError):
        calculate_average_daily_expenses(expenses=[])


def test__calculate_average_daily_expenses__today_float_expense(expense_fix):
    with pytest.raises(TypeError):
        list_exp_today_yesterday = [expense_fix(amount=10.2)]

        calculate_average_daily_expenses(expenses=list_exp_today_yesterday)


def test__calculate_average_daily_expenses__today_one_expense(expense_fix):
    list_exp_today = [expense_fix()]

    func = calculate_average_daily_expenses(expenses=list_exp_today)

    assert func == 5


def test__calculate_average_daily_expenses__today_yesterday_two_expense(date_fix, expense_fix):
    list_exp_today_yesterday = [expense_fix(),
                                expense_fix(amount=10,spent_at=date_fix.yesterday)]

    func = calculate_average_daily_expenses(expenses=list_exp_today_yesterday)

    assert func == 7.5


def test__calculate_average_daily_expenses__today_two_expense(expense_fix):
    list_exp_today_yesterday = [expense_fix(),
                                expense_fix(amount=10)]

    func = calculate_average_daily_expenses(expenses=list_exp_today_yesterday)

    assert func == 15


def test__calculate_average_daily_expenses__tomorrow_one_expense(date_fix, expense_fix):
    list_exp_today_yesterday = [expense_fix(spent_at=date_fix.tomorrow), expense_fix(amount=10)]

    func = calculate_average_daily_expenses(expenses=list_exp_today_yesterday)

    assert func == 7.5


def test__calculate_average_daily_expenses__old_year_one_expense(date_fix, expense_fix):
    list_exp_today_yesterday = [expense_fix(spent_at=date_fix.old_year), expense_fix(amount=10)]

    func = calculate_average_daily_expenses(expenses=list_exp_today_yesterday)

    assert func == 7.5
