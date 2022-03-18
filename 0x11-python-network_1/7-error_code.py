#!/usr/bin/python3
"""
Python script takes in a URL, send request and
to display the body of response
if HTTP status is > 400, please error code
"""
import requests
import sys
# import requests.HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)

    if resp.status_code < 400:
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
