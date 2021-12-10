#!/usr/bin/python3
""" Square module
"""


class Square:
    """ Define a Square class
    """
    def __init__(self, size=0):
        """ Initialized  methode that store the size od square """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ The methode area returns area of square """
        return int(self.__size) * int(self.__size)
