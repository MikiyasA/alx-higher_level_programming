#!/usr/bin/python3
"""
Python script to display the value of X-Request-ID
"""
import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
