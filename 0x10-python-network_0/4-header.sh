#!/bin/bash
# Bash script that takes in a URL, sends GET request to that URL, and displays the only body with header variable X-School-Usr-ID
curl -s "$1" -H "X-School-User-Id: 98"
