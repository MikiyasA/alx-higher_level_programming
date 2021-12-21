#!/usr/bin/python3
"""
The module to write string to the file
Using: def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """ The method writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename: a file name to write to
        text: text to be write
    Return:
        No. of character writen
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
