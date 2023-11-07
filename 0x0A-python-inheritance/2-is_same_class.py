#!/usr/bin/python3
"""checks if object is instance of class"""


def is_same_class(obj, a_class):
    """return true if obj is instance of class, otherwise false"""
    return type(obj) is a_class
