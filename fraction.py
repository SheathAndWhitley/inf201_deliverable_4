from math import gcd


class Fraction:
    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    @staticmethod
    def _coerce(other):
        if isinstance(other, Fraction):
            return other
        if isinstance(other, int):
            return Fraction(other)
        return None

    # Comparisons
    def __eq__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __lt__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    # Other special methods
    def __add__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
