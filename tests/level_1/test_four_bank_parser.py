import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test__parse_ineco_expense__success_case():
    
    assert parse_ineco_expense(
        sms=SmsMessage(text='Payment 100 AMD, 1234567890123456 22.11.23 00:00 xxx authcode xxxxxxx', 
        author='vasili',sent_at=datetime.datetime(2023, 11, 22, 0, 0)),
        cards=[BankCard(last_digits='3456', owner='vasia')]) == Expense(
            amount=decimal.Decimal('100'),
            card=BankCard(last_digits='3456',
                          owner='vasia'),
                          spent_in='xxx',
                          spent_at=datetime.datetime(2023, 11, 22, 0, 0))
    