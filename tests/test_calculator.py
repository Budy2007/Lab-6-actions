import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# add
def test_add_positive(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-2, -3) == -5

def test_add_zero(calc):
    assert calc.add(7, 0) == 7


# subtract
def test_subtract_positive(calc):
    assert calc.subtract(5, 3) == 2

def test_subtract_negative_result(calc):
    assert calc.subtract(3, 5) == -2

def test_subtract_zero(calc):
    assert calc.subtract(4, 0) == 4


# multiply
def test_multiply_positive(calc):
    assert calc.multiply(4, 3) == 12

def test_multiply_by_zero(calc):
    assert calc.multiply(9, 0) == 0

def test_multiply_negative(calc):
    assert calc.multiply(-4, 3) == -12


# divide
def test_divide_exact(calc):
    assert calc.divide(10, 2) == 5

def test_divide_fraction(calc):
    assert calc.divide(1, 4) == 0.25

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
