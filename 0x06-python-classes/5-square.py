#!/usr/bin/python3
""" Square module
"""


class Square:
    """ Define a Square class
    """
    def __init__(self, size):
        """ Intialize methonds that store the size of the square. """
        self.__size = size

    @property
    def size(self):
        """ property for method size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for method size """
        self.__size = value

    def area(self):
        """ The methode area returns area of square """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            return int(self.__size) * int(self.__size)

    def my_print(self):
        """ The function that prints  the square with the character # """
        if self.__size == 0:
            print()
        for p in range(self.__size):
            print("#" * self.__size)
