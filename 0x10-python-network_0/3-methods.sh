#!/bin/bash
# Bash script that takes in a URL,display the methond that the server will acceprts
curl -sIX OPTIONS "$1" | grep "ALLOW:" | cut -d " " -f 2-
