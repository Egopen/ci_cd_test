import pytest
from main import add, subtract, multiply, divide, is_prime_number


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
    (10.5, 4.5, 15.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (7.5, 2.5, 5.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (2.5, 2, 5.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, 3, -2),
    (5.0, 2.5, 2.0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = divide(10, 0)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (1, False),
    (0, False),
    (-5, False),
])
def test_is_prime_number(n, expected):
    assert is_prime_number(n) == expected
