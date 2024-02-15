'''My Calculator Test'''
from calculator import Calculator
import pytest

def test_addition():
    '''Test that addition function works.'''
    assert Calculator.perform_operation('add', 2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works.'''
    assert Calculator.perform_operation('subtract', 2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works.'''
    assert Calculator.perform_operation('multiply', 2, 2) == 4

def test_division():
    '''Test that division function works.'''
    assert Calculator.perform_operation('divide', 2, 2) == 1

def test_division_by_zero():
    '''Test that division by zero raises ValueError.'''
    with pytest.raises(ValueError):
        Calculator.perform_operation('divide', 1, 0)
