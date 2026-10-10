import pytest
from calculator import add, subtract, multiply, divide, heat_index_category


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


@pytest.mark.parametrize("temp, expected", [
    (39.9, "Normal"), (40, "Hot"), (45, "Heatwave"), (47, "Severe heatwave"),
])
def test_heat_index_category(temp, expected):
    assert heat_index_category(temp) == expected
