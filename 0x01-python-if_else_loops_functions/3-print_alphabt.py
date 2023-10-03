#!/usr/bin/python3
for ch in range(97, 122+1):
    if not (ch == 101 or ch == 113):
        print("{}".format(chr(ch)), end="")
