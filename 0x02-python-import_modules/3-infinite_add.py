#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argcount = len(argv) - 1
    sum = 0

    for a in range(1, argcount + 1):
        sum += int(argv[a])
    print("{}".format(sum))
