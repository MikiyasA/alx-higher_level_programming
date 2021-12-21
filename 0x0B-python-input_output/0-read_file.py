#!/usr/bin/python3
"""
The Module to read a file and print our to stdout
Using: def read_file(filename=""):
"""


def read_file(filename=""):
    """ the methond which read a text file with UTF8
        and print it to stdour
    Args:
       filename: a file name to be readed
    """
    with open(filename, encoding="utf-8") as r:
        print(r.read(), end="")
