#!/usr/bin/python3
"""
This is a function that prints a square shape with #-symbol
"""
def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise  TypeError("size must be an integer")
    if size > 0:
        print("#" * size + "\n") * size, end="")
