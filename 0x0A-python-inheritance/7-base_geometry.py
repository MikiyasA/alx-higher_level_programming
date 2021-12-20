#!/usr/bin/python3
"""

The module holds BaseGeometry class

"""


class BaseGeometry:
    """ A BaseGeometry class holds the mothod area
    """
    def area(self):
        """ A method the raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A method tha validate the value
        Args:
            name: name of the object
            value: value of the object
        Exceptions:
            TypeError
            ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
