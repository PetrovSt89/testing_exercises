import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


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

