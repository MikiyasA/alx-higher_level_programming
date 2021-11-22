#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    n_list = my_list[:]
    if idx >= 0 and idx < n:
        n_list[idx] = element
    return (n_list)
