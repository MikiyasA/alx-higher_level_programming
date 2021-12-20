#!/usr/bin/python3
"""
The module import BaseGeometry and use it as super class

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class inherits from BaseGeometry supper class """
    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ The method return the area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ The method that return printable string """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
