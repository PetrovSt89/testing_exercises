import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense, print_hello
from unittest.mock import patch, Mock


amount = 100
raw_card = "1234567890123456"
raw_date = "22.11.23"
raw_time = "00:00"
spent_in='xxx'
full_string = f'Payment {amount} AMD, {raw_card} {raw_date} {raw_time} {spent_in} authcode xxxxxxx'

def test__parse_ineco_expense__success_case():
    assert parse_ineco_expense(
        sms=SmsMessage(text=full_string, 
        author='vasili',sent_at=datetime.datetime(2023, 11, 22, 0, 0)),
        cards=[BankCard(last_digits='3456', owner='vasia')]) == Expense(
            amount=decimal.Decimal('100'),
            card=BankCard(last_digits='3456',
                          owner='vasia'),
                          spent_in='xxx',
                          spent_at=datetime.datetime(2023, 11, 22, 0, 0))


def xren_stub(x):
    m = Mock(return_value=10)
    return m.return_value


def test__print_hello__print():
    with (
        patch(target='functions.level_1.four_bank_parser.print') as print_mock,
        patch('functions.level_1.four_bank_parser.xren', new=xren_stub) as xren_mock,
    ):
        print_hello()
        print_mock.assert_called_once_with('Hello 10')


def test__print_hello__print_without_new():
    with (
        patch(target='functions.level_1.four_bank_parser.print') as print_mock,
        patch('functions.level_1.four_bank_parser.xren') as xren_mock,
    ):
        xren_mock.return_value = 10
        print_hello()
        print_mock.assert_called_once_with('Hello 10')

