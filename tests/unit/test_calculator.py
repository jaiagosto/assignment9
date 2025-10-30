# tests/unit/test_calculator.py

import pytest
from typing import Union
from app.operations import add, subtract, multiply, divide

Number = Union[int, float]

# ---------------------------------------------
# Unit Tests for Addition
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Adding two positive integers
        (-2, -3, -5),        # Adding two negative integers
        (2.5, 3.5, 6.0),     # Adding two positive floats
        (-2.5, 3.5, 1.0),    # Adding negative and positive float
        (0, 0, 0),           # Adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Testing the add function with different number combinations.
    """
    result = add(a, b)
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Unit Tests for Subtraction
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Subtracting positive integers
        (-5, -3, -2),        # Subtracting negative integers
        (5.5, 2.5, 3.0),     # Subtracting positive floats
        (-5.5, -2.5, -3.0),  # Subtracting negative floats
        (0, 0, 0),           # Subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Testing the subtract function with different number combinations.
    """
    result = subtract(a, b)
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Unit Tests for Multiplication
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Multiplying positive integers
        (-2, 3, -6),         # Multiplying negative and positive integer
        (2.5, 4.0, 10.0),    # Multiplying positive floats
        (-2.5, 4.0, -10.0),  # Multiplying negative and positive float
        (0, 5, 0),           # Multiplying by zero
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Testing the multiply function with different number combinations.
    """
    result = multiply(a, b)
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Unit Tests for Division
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Dividing positive integers
        (-6, 3, -2.0),         # Dividing negative by positive
        (6.0, 3.0, 2.0),       # Dividing positive floats
        (-6.0, 3.0, -2.0),     # Dividing negative by positive float
        (0, 5, 0.0),           # Dividing zero by a number
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Testing the divide function with different number combinations.
    """
    result = divide(a, b)
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Test for Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Testing that dividing by zero raises a ValueError.
    """
    # Check that dividing by zero raises the right error
    with pytest.raises(ValueError) as excinfo:
        divide(6, 0)
    
    # Make sure the error message is correct
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"