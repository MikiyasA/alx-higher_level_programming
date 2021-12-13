#!/usr/bin/python3
"""

The moduel that defines the Rectangle class


"""


class Rectangle:
    """ The Rectangle class which will holds with and height methods
    """
    def __init__(self, width=0, height=0):
        """ Initialized method that store width of rectangle.
        Args:
            width: width of rectangle
            height: height of rectange
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property for method width.
        Return:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for mothode width.
        Args:
            value: width
        Exceptions:
            TypeError: width must be an integer
            ValueError: width must be >=0
        """
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Property for method height
        Return:
             height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for method hieght.
        Args:
            value: height
        Exceptions:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """ The method calculates area of the rectangle
        Return:
            area = width * height
        """
        a = (self.width * self.height)
        return a

    def perimeter(self):
        """ The method calculates perimeter of the rectangle
        Return:
             perimeter (p) = 2(width + height)
        """
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = ((self.width * 2) + (self.height * 2))
        return (p)

    def __str__(self):
        """ The mothod that return the rectangle '#'
        using width & height
        Return:
             rec - rectangle

        """
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        for i in range(self.height):
            rec += ("#" * self.width) + '\n'
        return rec[:-1]

    def __repr__(self):
        """
        The method that return ssring representation of the instance
        Returns:
            string represantation of the object
        """
        return("Rectangle({}, {})".format(self.width, self.height))
