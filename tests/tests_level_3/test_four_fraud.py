from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__success(expense_fix, date_fix):

    list_exp = [expense_fix(spent_at=date_fix.september),
                expense_fix(spent_at=date_fix.september),
                expense_fix(spent_at=date_fix.september)]

    fraud = find_fraud_expenses(history=list_exp)
    
    assert fraud == list_exp


def test__find_fraud_expenses__amount_more_then_5000(expense_fix):

    list_exp = [expense_fix(amount=5001),
                expense_fix(amount=5001),
                expense_fix(amount=5001)]

    fraud = find_fraud_expenses(history=list_exp)
    
    assert fraud == []


def test__find_fraud_expenses__transactions_amount_less_then_3(expense_fix, date_fix):

    list_exp = [expense_fix(spent_in='hhz', spent_at=date_fix.october),
                expense_fix(spent_in='hzz', spent_at=date_fix.september),
                expense_fix(spent_in='hzz', spent_at=date_fix.october)]

    fraud = find_fraud_expenses(history=list_exp)
    
    assert fraud == []


def test__find_fraud_expenses__empty_history():    
    assert find_fraud_expenses(history=[]) == []