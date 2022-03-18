#!/usr/bin/python3
"""
Python script takes in a leter and send POST
"""
import requests
import sys


if __name__ == "__main__":
    d = {'q': ""}

    try:
        d['q'] = sys.argv[1]
    except:
        pass

    reqt = requests.post('http://0.0.0.0:5000/search_user', d)

    try:
        jn = reqt.json()
        if not jn:
            print("No result")
        else:
            print("[{}] {}".format(jn.get('id'), jn.get('name')))
    except:
        print("Not a valid JSON")
