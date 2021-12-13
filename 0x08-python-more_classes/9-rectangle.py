#!/usr/bin/python3
"""

The moduel that defines the Rectangle class


"""


class Rectangle:
    """ The Rectangle class which will holds with and height methods
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialized method that store width of rectangle.
        Args:
            width: width of rectangle
            height: height of rectange
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
            rec += (str(self.print_symbol) * self.width) + '\n'
        return rec[:-1]

    def __repr__(self):
        """
        The method that return ssring representation of the instance
        Returns:
            string represantation of the object
        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ This method is called when we delete an object
        Return:
          Bye rectangle...
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """ The method returns the largest rectangle using area function
        Args:
           rect_1: the first rectangle to be compared
           rect_2: the second rectangle to be compared
        Reurns:
           The largest rectangle
        Exception:
            TypeError: rect_1 and rect_2 must be instance of rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        v_rect_1 = Rectangle.area(rect_1)
        v_rect_2 = Rectangle.area(rect_2)

        if v_rect_1 > v_rect_2:
            return rect_1
        elif v_rect_1 < v_rect_2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ The classmethod returns Rectangle instance
        with width == height == size
        Args:
           size: size of quare
        Return:
             width == height == size
        """

        return (cls(size, size))
