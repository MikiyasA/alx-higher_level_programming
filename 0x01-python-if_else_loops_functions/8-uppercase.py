#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) in range(97, 123):
            n = 32
        else:
            n = 0
        print("{:c}" .format(ord(w) - n), end="")
    print()
