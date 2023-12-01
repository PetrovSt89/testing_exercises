from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__discriminant_less_then_0():
    assert solve_square_equation(
    square_coefficient=1.0,
    linear_coefficient=1.0,
    const_coefficient=1.0,
    ) == (None, None)


def test__solve_square_equation__not_square_coefficient():
    assert solve_square_equation(
    square_coefficient=0.0,
    linear_coefficient=1.0,
    const_coefficient=1.0,
    ) == (-1.0, None)


def test__solve_square_equation__not_square_coefficient_not_linear_coefficient():
    assert solve_square_equation(
    square_coefficient=0.0,
    linear_coefficient=0.0,
    const_coefficient=1.0,
    ) == (None, None)


def test__solve_square_equation__discriminant_is_0():
    assert solve_square_equation(
    square_coefficient=2.0,
    linear_coefficient=4.0,
    const_coefficient=2.0,
    ) == (-1.0, -1.0)


def test__solve_square_equation__discriminant_more_then_0():
    assert solve_square_equation(
    square_coefficient=1.0,
    linear_coefficient=6.0,
    const_coefficient=5.0,
    ) == (-5.0, -1.0)

