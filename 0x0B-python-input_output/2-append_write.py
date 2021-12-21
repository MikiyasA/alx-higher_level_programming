#!/usr/bin/python3
"""
The module to append string to the file
def append_write(filename="", text=""):
"""


def append_write(filename="", text=""):
    """ The method append a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename: a file name to write to
        text: text to be write
    Return:
        No. of character writen
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
