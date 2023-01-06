#!/usr/bin/python3
from sys import argv

a = 0
for s in argv[1:]:
    a += int(s)
print("{:d}".format(a))
