#!/usr/bin/python3
"""
Scrpt thatl list all satate from DB
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE CONVERT(`name` USING latin1)\
    COLLATE Latin1_General_CS LIKE '{}'".format(sys.argv[4]))
    states = cur.fetchall()
    for s in states:
        print(s)
