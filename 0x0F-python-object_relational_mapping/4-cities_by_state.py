#!/usr/bin/python3
"""
Functiion to list all cities of the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], a=sys.argv[3])
    b = a.cursor()
    b.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in b.fetchall()]
