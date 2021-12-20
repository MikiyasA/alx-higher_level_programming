#!/usr/bin/python3
"""
The module holds MyInt that inherits from int

"""


class MyInt(int):
    """
    MyInt class
    """
    def __eq__(self, other):
        """ The method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ The method that returns == check """
        return int.__eq__(self, other)
