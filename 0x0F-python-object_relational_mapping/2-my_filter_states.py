#!/usr/bin/python3
"""
Function to display all values in the states table of the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], a=sys.argv[3])
    c = a.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    a.close()
