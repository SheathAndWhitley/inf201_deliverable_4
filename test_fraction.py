import pytest
from fraction import Fraction


def test_init_reduces_and_normalises_sign():
    f = Fraction(2, -4)
    assert (f.numerator, f.denominator) == (-1, 2)


def test_init_default_denominator():
    assert Fraction(3).denominator == 1


def test_init_invalid():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


def test_comparisons():
    a, b = Fraction(1, 2), Fraction(2, 3)
    assert a == Fraction(2, 4)
    assert a != b
    assert a < b
    assert a <= b and a <= Fraction(1, 2)
    assert b > a
    assert b >= a and b >= Fraction(4, 6)
    assert Fraction(4, 2) == 2


def test_arithmetic():
    a, b = Fraction(1, 2), Fraction(1, 3)
    assert a + b == Fraction(5, 6)
    assert a - b == Fraction(1, 6)
    assert a * b == Fraction(1, 6)
    assert a / b == Fraction(3, 2)
    with pytest.raises(ZeroDivisionError):
        a / Fraction(0)


def test_float():
    assert float(Fraction(1, 4)) == 0.25


def test_str_and_repr():
    assert str(Fraction(3, 4)) == "3/4"
    assert repr(Fraction(3, 4)) == "Fraction(3, 4)"
