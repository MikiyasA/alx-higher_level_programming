#!/usr/bin/python3
for a in reversed(range(97, 123)):
    print("{:c}" .format(a if (a % 2 == 0) else (a - 32)), end="")
