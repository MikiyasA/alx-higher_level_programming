#!/usr/bin/python3
"""
The module returns the JSON representation of an object (string):
Using: def to_json_string(my_obj):
"""

import json


def to_json_string(my_obj):
    """ The method returns the JSON representation of an object (string):
    Args:
        my_obje: the object to to be represented as JSON
    """
    return json.dumps(my_obj)
