#!/usr/bin/python3
"""
Th module hold the method to add new atribute

"""


def add_attribute(object, name, value):
    """ The method adds a new attribute to an object if it’s possible
    Args:
        object: an object
        name: name of atribute to be added
        value: value of atribute to be added
    Exception:
        TypeError: can't add new attribute
    """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
