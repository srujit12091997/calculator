# test_calculator.py
'''My Calculator Test'''
from decimal import Decimal
from calculator import Calculator

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4'), "Addition result is incorrect"

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0'), "Subtraction result is incorrect"

def test_divide():
    '''Test that division function works'''
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1'), "Division result is incorrect"

def test_multiply():
    '''Test that multiplication function works'''
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4'), "Multiplication result is incorrect"
