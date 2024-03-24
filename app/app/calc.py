"""
Calculate functions
"""


def add(x, y):
    """Add x and y and return result."""
    return x + y


def subtract(x, y):
    """Subtract x from y and return result."""
    return x - y


def fib_numbers(x):
    """Gives fibonacci number at requested index."""
    end = x
    a, b = 0, 1
    while end > 0:
        a, b = b, a+b
        end -= 1
    return a
