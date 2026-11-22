TOL = 1e-9
UNITS = ("C", "F", "K")


class Temperature:
    def __init__(self, value, unit="C"):
        unit = str(unit).upper()
        if unit not in UNITS:
            raise ValueError(f"Invalid unit: {unit}")
        self._value = float(value)
        self._unit = unit
        if self.to_kelvin() < -TOL:
            raise ValueError("Temperature below absolute zero")

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_celsius(self) -> float:
        if self._unit == "K":
            return self._value - 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value

    def to_fahrenheit(self) -> float:
        if self._unit == "C":
            return self._value * 9 / 5 + 32
        if self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32
        return self._value

    def to_kelvin(self) -> float:
        if self._unit == "C":
            return self._value + 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        return self._value

    def convert_to(self, target_unit: str) -> "Temperature":
        target = str(target_unit).upper()
        if target == "C":
            return Temperature(self.to_celsius(), "C")
        if target == "F":
            return Temperature(self.to_fahrenheit(), "F")
        if target == "K":
            return Temperature(self.to_kelvin(), "K")
        raise ValueError(f"Invalid unit: {target_unit}")

    def __repr__(self) -> str:
        return f"Temperature({self._value!r}, {self._unit!r})"

    def __str__(self) -> str:
        symbol = "K" if self._unit == "K" else f"°{self._unit}"
        return f"{self._value:.2f} {symbol}"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) <= TOL

    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() and not self == other

    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return other < self

    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return other <= self
