#!/usr/bin/python3
"""
Function to Liss all states from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], a=sys.argv[3])
    c = a.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
