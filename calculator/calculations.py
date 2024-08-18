"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


def add(a: float | int, b: float | int) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: float | int, b: float | int) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Returns:
        float: A number representing the arithmetic difference of `a` and `b`.
    """
    return float(a - b)

def multiply(a: float | int, b: float | int) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a * b)

def divide(a: float | int, b: float | int) -> float:
    """Compute and return the division of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Returns:
        float: A number representing the division of `a` by `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
