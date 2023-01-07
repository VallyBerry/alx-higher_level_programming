#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    from sys import argv

    a = 0
    for s in argv[1:]:
        a += int(s)
    print("{:d}".format(a))
