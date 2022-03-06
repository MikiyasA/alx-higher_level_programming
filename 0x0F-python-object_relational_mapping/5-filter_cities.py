#!/usr/bin/python3
"""
Scrpt thatl list all satate from DB
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    nm = (sys.argv[4],)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name=%s", nm)
    states = cur.fetchall()

    print(", ".join([s[1] for s in states]))
