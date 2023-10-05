#!/usr/bin/python3
import sys

argcount = len(sys.argv) - 1

if argcount == 1:
    print("{} argument:".format(argcount))
elif argcount == 0:
    print("{} arguments.".format(argcount))
else:
    print("{} arguments:".format(argcount))

for a in range(1, argcount + 1):
    print("{}: {}".format(a, sys.argv[a]))
