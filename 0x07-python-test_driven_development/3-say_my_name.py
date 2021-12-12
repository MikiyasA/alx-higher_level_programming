#!/usr/bin/python3
""" A module to print first and last name as below format
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ A function to print out first name and last name in formated way.

    Args:
       first_name:
       last_name:
    exception:
       TypeError: first_name must be a string
       TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
