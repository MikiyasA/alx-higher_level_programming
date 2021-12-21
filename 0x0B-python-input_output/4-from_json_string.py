#!/usr/bin/python3
"""
The module returns an object (Python data structure)
represented by a JSON string:
Using: def from_json_string(my_str):
"""

import json


def from_json_string(my_str):
    """ The method  returns an object (Python data structure)
    represented by a JSON string:
    Args:
       my_str: the string
    """
    return json.loads(my_str)
