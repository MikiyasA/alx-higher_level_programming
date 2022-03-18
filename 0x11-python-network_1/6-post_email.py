#!/usr/bin/python3
"""
Python script takes URL
    send a POST request to passed url with email
    display the body of the respornse
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    d = {'email': sys.argv[2]}

    reqt = requests.post(url, data=d)
    print(reqt.text)
