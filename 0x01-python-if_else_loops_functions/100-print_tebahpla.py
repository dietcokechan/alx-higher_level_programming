#!/usr/bin/python3
for c in range(122, 97-1, -1):
    if c % 2 == 1:
        c -= 32;
    print("{:s}".format(chr(c)), end="")
