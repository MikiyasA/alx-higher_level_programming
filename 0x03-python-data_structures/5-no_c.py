#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for el in range(len(my_string)):
        if my_string[el] != 'c' and my_string[el] != 'C':
            new_string = new_string + my_string[el]
    return new_string
