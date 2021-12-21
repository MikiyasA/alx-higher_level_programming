#!/usr/bin/python3
"""
The module that writes an Object to a text file,
using a JSON representation:
Using: def save_to_json_file(my_obj, filename):
"""

import json


def save_to_json_file(my_obj, filename):
    """ The method that writes an Object to a text file,
    using a JSON representation:
    Args:
         my_obj: an object
         filename: text file name
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
