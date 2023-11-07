#!/usr/bin/python3
"""checks if object is an instance of a class"""


def inherits_from(obj, a_class):
    """returns true or false"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
