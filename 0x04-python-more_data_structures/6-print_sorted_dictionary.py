#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary != None:
        for k, v in sorted(a_dictionary.items()):
            print("{}: {}" .format(k, v))
