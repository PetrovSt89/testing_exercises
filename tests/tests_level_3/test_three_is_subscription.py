from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__true(expense_fix, date_fix):
    exp_1 = expense_fix()
    exp_2 = expense_fix(spent_at=date_fix.september)
    exp_3 = expense_fix(spent_at=date_fix.october)
    history = [exp_1, exp_2, exp_3]

    func = is_subscription(expense=exp_1, history=history)

    assert func == True


def test__is_subscription__month_more_then_one(expense_fix, date_fix):
    exp_1 = expense_fix()
    exp_2 = expense_fix(amount=10)
    exp_3 = expense_fix(spent_at=date_fix.october)
    history = [exp_1, exp_2, exp_3]

    func = is_subscription(expense=exp_1, history=history)

    assert func == False


def test__is_subscription__expenses_less_then_three(expense_fix):
    exp_1 = expense_fix()
    exp_2 = expense_fix(amount=10)
    history = [exp_1, exp_2]

    func = is_subscription(expense=exp_1, history=history)

    assert func == False


def test__is_subscription__no_expense(expense_fix, date_fix):
    exp_1 = expense_fix()
    exp_2 = expense_fix(spent_in='hzz', spent_at=date_fix.september)
    exp_3 = expense_fix(spent_in='hhz', spent_at=date_fix.october)
    exp_4 = expense_fix(spent_in='hzz', spent_at=date_fix.october)
    history = [exp_2, exp_3, exp_4]

    func = is_subscription(expense=exp_1, history=history)

    assert func == False