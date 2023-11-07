#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """define class"""
    def __init__(self, value):
        """initialize class"""
        self.value = value

    def __eq__(self, b):
        """reverse equal to not equal"""
        return self.value != b

    def __ne__(self, b):
        """reverse not equal to equal"""
        return self.value == b
