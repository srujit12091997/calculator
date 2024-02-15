'''My Calculator Test'''
from calculator import add, subtract, multiply, divide
import pytest

def test_addition():
    '''Test that the addition function works correctly.'''
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtraction():
    '''Test that the subtraction function works correctly.'''
    assert subtract(2, 2) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiplication():
    '''Test that the multiplication function works correctly.'''
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_division():
    '''Test that the division function works correctly.'''
    assert divide(4, 2) == 2
    assert divide(-2, 1) == -2
    assert divide(-2, -1) == 2

def test_division_by_zero():
    '''Test that dividing by zero raises a ValueError.'''
    with pytest.raises(ValueError):
        divide(1, 0)
