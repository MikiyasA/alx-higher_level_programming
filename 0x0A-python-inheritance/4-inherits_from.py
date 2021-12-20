#!/usr/bin/python3
"""
The module to check if the object is inherited from a class
Using: def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """ The method to check if obj is instance of class
    inherited from specific calss
    Args:
        obj: an object
        a_class: class type
    Return:
        True: if the object is an instance of a class that inherited
              (directly or indirectly) from the specified class
        False: otherwise
    """
    if type(obj) is a_class:
        return False
    return (isinstance(obj, a_class))
