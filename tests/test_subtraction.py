import unittest 
from src.subtraction import Subtraction

def test_subtraction_positive_numbers():
    """Test subtraction with positive numbers."""
    subtraction = Subtraction(10, 5)
    assert subtraction.calculate() == 5

def test_subtraction_negative_numbers():
    """Test subtraction with negative numbers."""
    subtraction = Subtraction(-10, -5)
    assert subtraction.calculate() == -5

def test_subtraction_mixed_numbers():
    """Test subtraction with mixed positive and negative numbers."""
    subtraction = Subtraction(10, -5)
    assert subtraction.calculate() == 15

def test_subtraction_with_zero():
    """Test subtraction where one number is zero."""
    subtraction = Subtraction(10, 0)
    assert subtraction.calculate() == 10
    subtraction = Subtraction(0, 10)
    assert subtraction.calculate() == -10
