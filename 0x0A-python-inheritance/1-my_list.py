#!/usr/bin/python3
"""class derived from list"""


class MyList(list):
    """initialize class"""
    def print_sorted(self):
        print(sorted(self))
