#!/usr/bin/python3
"""student class"""


class Student:
    """define class"""
    def __init__(self, first_name, last_name, age):
        """initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """prints __dict__"""
        if (isinstance(attrs, list) and all(isinstance(i, str) for i in attrs)):
            return ({i: j for i, j in self.__dict__.items() if i in attrs})
        else:
            return self.__dict__
