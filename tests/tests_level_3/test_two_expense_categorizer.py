from functions.level_3.two_expense_categorizer import guess_expense_category
from functions.level_3.models import ExpenseCategory


def test__guess_expense_category__no_trigger(expense_fix):
    assert guess_expense_category(expense=expense_fix()) is None


def test__guess_expense_category__triggers_equal_spent_in(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="asador")
        ) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__startswith(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="meat house-hz")
        ) == ExpenseCategory.SUPERMARKET


def test__guess_expense_category__endswith(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="hz.netflix")
        ) == ExpenseCategory.ONLINE_SUBSCRIPTIONS
    

def test__guess_expense_category__endswith_2(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="hz pharm")
        ) == ExpenseCategory.MEDICINE_PHARMACY
    

def test__guess_expense_category__endswith_3(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="hz,pharm")
        ) == ExpenseCategory.MEDICINE_PHARMACY


def test__guess_expense_category__startswith_2(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="cinema galleria/hz")
        ) == ExpenseCategory.THEATRES_MOVIES_CULTURE
    

def test__guess_expense_category__startswith_3(expense_fix):
    assert guess_expense_category(
        expense=expense_fix(spent_in="cinema galleria\\hz")
        ) == ExpenseCategory.THEATRES_MOVIES_CULTURE