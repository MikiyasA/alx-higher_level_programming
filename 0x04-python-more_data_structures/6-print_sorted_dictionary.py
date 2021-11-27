#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_o = list(a_dictionary.keys())
    list_o.sort()

    for k in list_o:
        print("{}: {}" .format(k, a_dictionary.get(k)))
