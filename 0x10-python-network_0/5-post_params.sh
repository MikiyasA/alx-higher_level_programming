#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the only body of 200 status
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
