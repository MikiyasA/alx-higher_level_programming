#!/usr/bin/python3
"""
The module import subclass Rectangle anf use it as sub.subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The class Square inhetirs from Rectangle """

    def __init__(self, size):
        """ Initializes the instances """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ The method returns area of square """
        return (super().area())

    def __str__(self):
        """ The method that return printable string """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
