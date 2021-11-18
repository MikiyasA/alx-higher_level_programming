#!/usr/bin/python3
import sys
if __name__ == "__main__":

    n = len(sys.argv)
    add = 0

    for i in range(1, n):
        add += int(sys.argv[i])
    print(add)
