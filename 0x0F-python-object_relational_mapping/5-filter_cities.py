#!/usr/bin/python3
"""
Function to display all cities of a given state from the
states table of the.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], a=sys.argv[3])
    b = a.cursor()
    b.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in b.fetchall() if ct[4] == sys.argv[4]]))
