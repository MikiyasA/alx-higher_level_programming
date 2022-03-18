#!/usr/bin/python3
"""
Python script to display the value of X-Request-ID
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        html_id = resp.info().get('X-Request-Id')
        print(html_id)
