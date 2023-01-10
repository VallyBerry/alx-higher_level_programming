#!/usr/bin/python3


'''replaces an element at a given position without modifying the list'''


def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
