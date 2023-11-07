#!/usr/bin/python3
"""looks up attr and methods of obj"""


def lookup(obj):
    """returns list of attr and methods of obj"""
    return [i for i in dir(obj)]
