#!/usr/bin/python3
"""
The module holds a class Square that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Intializatation from super class Rectangle """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ property for size
        Returns:
             size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size
        Args:
            value: value of size """
        self.width = value
        self.height = value

    def __str__(self):
        """The method __str__ to print as below returns
        Returns:[Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ the method update that assigns attributes
        Args:
           args: list of argument
           kwargs: keyworde argument
        """
        lists = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, lists[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ The methon that returns the
        dictionary representation of a Square
        """
        dictry = {'id': self.id, 'x': self.x,
                  'size': self.size, 'y': self.y}
        return (dictry)
