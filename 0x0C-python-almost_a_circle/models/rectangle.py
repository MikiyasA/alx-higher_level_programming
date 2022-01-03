#!/usr/bin/python3
"""
8The module rectangls hold class Rectangle
inherits from Base

"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize width, height, x and y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Property for meyhod width
        Returns: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width
        Args:
             value: width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Property for height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height
        Args:
             value: height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ property for x
        Returns: x
        """
        return self.__x

    @x.setter
    def x(self, v):
        """ setter for x
        Args:
            v: vlaue of x
        """
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """ property for y
        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, v):
        """ setter for y
        Args:
            v: y
        """
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        """ The method area to calulate area of Rectangle
        Returns:
             area value of the Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """ The method display that print out Rectangle
        instance with character '#'
        """
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """ The method __str__ to print as below returns
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<geight>
        """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ The method update that assign an argument to each attribute
        """

        lists = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, lists[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ the method that returns the dictionary representation
        of a Rectangle
        """
        dictry = {'x': self.__x, 'y': self.__y, 'id': self.id,
                  'height': self.__height, 'width': self.__width}
        return (dictry)
