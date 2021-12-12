#!/usr/bin/python3
"""
The module add two intigers using methon def add_integer(a, b=98):
"""


def add_integer(a, b=98):
    """
    The function that adds two integer or/and float
    Args:
        a: first integer
        b: second integer
    Returns:
       addition of a and b
    Raises:
       TypeError: a or b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
