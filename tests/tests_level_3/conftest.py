import datetime
import dataclasses
import decimal
import pytest

from functions.level_3.models import Expense, ExpenseCategory, Currency, BankCard


@dataclasses.dataclass
class Date:
    day_delta: datetime = datetime.timedelta(days=1)
    today: datetime.datetime = datetime.datetime.now()
    yesterday: datetime.datetime = today - day_delta
    tomorrow: datetime.datetime = today + day_delta
    old_year: datetime.datetime = datetime.datetime.strptime(
        "1900-01-15 15:15", "%Y-%m-%d %H:%M")
    september: datetime.datetime = datetime.datetime.strptime(
        "2023-09-15 15:15", "%Y-%m-%d %H:%M")
    october: datetime.datetime = datetime.datetime.strptime(
        "2023-10-15 15:15", "%Y-%m-%d %H:%M")


@pytest.fixture
def date_fix():
    return Date()


@pytest.fixture
def expense_fix(date_fix: datetime.datetime):
    def exp(
        amount: decimal.Decimal=5, spent_in: str='hz', spent_at: datetime.datetime=date_fix.today, 
        category: ExpenseCategory | None = None):
        return Expense(amount=amount, currency=Currency.RUB, card=BankCard,
              spent_in=spent_in, spent_at=spent_at, category=category)

    return exp
