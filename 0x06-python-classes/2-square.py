#!/usr/bin/python3
""" Square module
"""


class Square:
    """ Define a Square class
    """
    def __init__(self, size=0):
        """ Intialize methonds that store the size of the square. """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
