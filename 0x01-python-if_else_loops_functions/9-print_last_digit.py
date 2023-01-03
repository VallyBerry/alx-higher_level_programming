#!/usr/bin/python3
def print_last_digit(number):
'''prints last digit of a number'''
a = abs(number % 10)
print('{}'.format(a), end='')
return a
