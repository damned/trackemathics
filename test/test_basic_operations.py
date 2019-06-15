import pytest
from trackemathics.value import Value

def test_addition():
    assert (Value(3) + Value(-8)).value == -5

def test_subtraction():
    assert (Value(15) - Value(7)).value == 8

def test_multiplication():
    assert (Value(5) * Value(3)).value == 15

def test_division():
    assert (Value(5) / Value(2)).value == 2.5
