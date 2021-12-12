#!/usr/bin/python3
""" The module to prince square with the character '#'
using def print_square(size): function """


def print_square(size):
    """ The function print size of square with '#'
    Args:
        size: size of equare 
    Exception:
        TypeError: size must be an integer
        ValueError: size must be >= 0
     """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
