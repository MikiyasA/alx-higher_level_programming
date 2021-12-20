#!/usr/bin/python3
"""
The module import BaseGeomerty and use is super class
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
