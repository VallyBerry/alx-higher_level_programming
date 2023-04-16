#!/usr/bin/python3
"""
function to display all values in the states table of the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], a=argv[3], charset="utf8")
    b = a.cursor()
    b.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = b.fetchall()
    for row in rows:
        print(row)
    b.close()
    a.close()
