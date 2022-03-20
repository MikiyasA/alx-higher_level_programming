#!/bin/bash
# Bash script that takes in a URL, sends delete  request to that URL, and displays the only body of 200 status
curl -sX DELETE "$1"
