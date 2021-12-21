#!/usr/bin/python3
"""
The module that creates an Object from a “JSON file”:
Using: def load_from_json_file(filename):
"""

import json


def load_from_json_file(filename):
    """ the method that creates an Object from a JSON file
    Args:
        filename: textfile name
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
