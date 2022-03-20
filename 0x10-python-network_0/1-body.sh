#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the only body of 200 status
curl -sL "$1"
