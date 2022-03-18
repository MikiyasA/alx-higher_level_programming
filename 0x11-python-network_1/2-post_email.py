#!/usr/bin/python3
"""
Python script to display the value of X-Request-ID
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value).encode('ascii')
    reqt = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(reqt) as resp:
        print(resp.read().decode('utf-8'))
