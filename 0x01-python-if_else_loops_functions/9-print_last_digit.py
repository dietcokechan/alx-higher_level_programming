#!/usr/bin/python3
def print_last_digit(number):
    abslastnum = abs(number) % 10
    print("{}".format(abslastnum), end="")
    return abslastnum
