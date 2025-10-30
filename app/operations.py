# app/operations.py
"""
Basic math operations for the calculator.
This module has the core functions: add, subtract, multiply, and divide.
"""
from typing import Union

# Number can be either an int or a float
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Adds two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    result = a + b
    return result

def subtract(a: Number, b: Number) -> Number:
    """
    Subtracts b from a.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
    
    Returns:
        The difference (a - b)
    """
    result = a - b
    return result

def multiply(a: Number, b: Number) -> Number:
    """
    Multiplies two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    result = a * b
    return result

def divide(a: Number, b: Number) -> float:
    """
    Divides a by b.
    
    Args:
        a: The dividend (number being divided)
        b: The divisor (number dividing by)
    
    Returns:
        The quotient as a float
    
    Raises:
        ValueError: If trying to divide by zero
    """
    # Can't divide by zero, so we check first
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    
    result = a / b
    return result
