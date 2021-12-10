#!/usr/bin/python3
""" Square module
"""


class Square:
    """ Define a Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Intialize methonds that store the size of the square. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ property for method size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for mothod size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Property for method position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for method position """
        self.__position = value

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ The methode area returns area of square """
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """ The function that prints the square with the character # """
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if self.size == 0:
            print()
        else:
            for q in range(self.position[1]):
                print()
            for p in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
