#!/usr/bin/python3
"""
The module import subclass Rectangle and use it as sub.subclasd
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
