#!/usr/bin/python3
"""
Python script takes GitHub credentials and
use the Github API to display
"""
import requests
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        reqt = requests.get(url)
        comt = reqt.json()

        for i in range(1000):
            print('{}: {}'.format(comt[i].get('sha'), comt[i].get('commit')
                                  .get('author').get('name')))
    except IndexError:
        pass
