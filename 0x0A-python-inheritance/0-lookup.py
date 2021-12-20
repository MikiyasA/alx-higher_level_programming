#!/usr/bin/python3
"""
The module returns returns the list of available
attributes and methods of an object:
Using: def lookup(obj):
"""


def lookup(obj):
    """ The method  returns the list of available
    attributes and methods of an object
    Args:
       obj - an object
    """
    return (dir(obj))
