import pytest
from temperature import Temperature

# (C, F, K)
REFERENCE_POINTS = [
    (-273.15, -459.67, 0.0),
    (-40.0, -40.0, 233.15),
    (0.0, 32.0, 273.15),
    (37.0, 98.6, 310.15),
    (100.0, 212.0, 373.15),
]


# 1. Initialization
def test_default_unit():
    assert Temperature(25).unit == "C"


@pytest.mark.parametrize("unit", ["c", "f", "k", "C", "F", "K"])
def test_case_insensitive_unit(unit):
    assert Temperature(300, unit).unit == unit.upper()


def test_read_only():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 10
    with pytest.raises(AttributeError):
        t.unit = "F"


# 2. Validation
@pytest.mark.parametrize("unit", ["X", "", "Celsius"])
def test_invalid_unit(unit):
    with pytest.raises(ValueError):
        Temperature(0, unit)


@pytest.mark.parametrize("value, unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)


def test_convert_to_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(0, "C").convert_to("X")


# 3. Conversions
@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversions(c, f, k):
    for t in (Temperature(c, "C"), Temperature(f, "F"), Temperature(k, "K")):
        assert t.to_celsius() == pytest.approx(c, abs=1e-9)
        assert t.to_fahrenheit() == pytest.approx(f, abs=1e-9)
        assert t.to_kelvin() == pytest.approx(k, abs=1e-9)


# 4. Round-trip
@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_round_trip(c, f, k):
    t = Temperature(c, "C")
    back = t.convert_to("f").convert_to("K").convert_to("c")
    assert back.unit == "C"
    assert back == t
    assert back.value == pytest.approx(c, abs=1e-9)


# 5. Cross-unit comparisons
def test_equality_mixed_units():
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(0, "C") != Temperature(1, "C")


def test_ordering_mixed_units():
    a, b = Temperature(0, "C"), Temperature(50, "F")
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    assert Temperature(100, "C") <= Temperature(212, "F")
    assert Temperature(100, "C") >= Temperature(212, "F")


def test_compare_with_non_temperature():
    t = Temperature(0, "C")
    assert t.__eq__(0) is NotImplemented
    assert t != 0
    with pytest.raises(TypeError):
        t < 0


# 6. Formatting
def test_str():
    assert str(Temperature(25, "C")) == "25.00 °C"
    assert str(Temperature(98.6, "f")) == "98.60 °F"
    assert str(Temperature(300, "K")) == "300.00 K"


def test_repr():
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
