#!/usr/bin/pthon3
"""
The module to check the object is an instance or instance  of a class
Using def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """ The method to check if the object is an instance of,
    or if the object is an instance of a class
    Args:
       obj: the object to be checked
       a_class: an instance of specified class
    Return:
       True: if the object is an instance of,
             or if the object is an instance of a class
       False: otherwise
    """
    return (isinstance(obj, a_class))
