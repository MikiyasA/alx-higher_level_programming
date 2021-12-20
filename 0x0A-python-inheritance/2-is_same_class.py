#!/usr/bin/pthon3
"""
The module to check instance of object
Using def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """ The method to check if the object is exactly
    an instance of the specified class
    Args:
       obj: the object to be checked
       a_class: an instance of specified class
    Return:
       True: if the object is exactly an instance of the specified class
       False: otherwise
    """
    return (type(obj) is a_class)
