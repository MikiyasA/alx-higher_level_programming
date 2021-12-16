#!/usr/bin/python3
"""
The module that prevents the user from dynamically
creating new instance attributes, except if the new
instance attribute is called first_name.
"""


class LockedClass:
    """
    The class prevent the unit to create new instance dynamically
    """

    __slots__ = ['first_name']

    def __init__(self):
        """ Intializing the method """
        pass
