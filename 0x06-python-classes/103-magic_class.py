#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    """Circle object"""
    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(self.__radius) is not int and type(self.__radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Get area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Get circumference of circle"""
        return 2 * math.pi * self.__radius
