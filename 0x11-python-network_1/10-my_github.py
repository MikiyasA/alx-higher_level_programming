#!/usr/bin/python3
"""
Python script takes GitHub credentials and
use the Github API to display 
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    usr = sys.argv[1]
    pss = sys.argv[2]
    reqt = requests.get(url, auth=requests.auth.HTTPBasicAuth(usr, pss))
    print(reqt.json().get('id'))
