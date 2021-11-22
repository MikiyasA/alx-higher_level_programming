#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    n_list = my_list[:]
    if idx < 0 or idx > n:
        return None
#    for i in range(n):
#        if i == idx:
    n_list[idx] = element
    return n_list
