#!/usr/bin/python3
"""student class"""


class Student:
    """define class"""
    def __init__(self, first_name, last_name, age):
        """initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """prints __dict__"""
        return self.__dict__
