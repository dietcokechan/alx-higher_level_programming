#!/usr/bin/python3
"""append text after line pattern in file"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
