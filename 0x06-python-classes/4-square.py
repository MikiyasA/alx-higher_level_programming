#!/usr/bin/python3
""" Square module
"""


class Square:
    """ Define a Square class
    """
    def __init__(self, size=0):
        """ Intialize methonds that store the size of the square. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ property for method size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for method size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ The methode area returns area of square """
        return int(self.__size) * int(self.__size)
