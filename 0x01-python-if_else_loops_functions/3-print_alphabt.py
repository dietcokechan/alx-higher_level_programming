#!/usr/bin/python3
for ch in range(97, 122+1):
    if ch != 101 or ch != 116:
        print("{}".format(chr(ch)), end="")
