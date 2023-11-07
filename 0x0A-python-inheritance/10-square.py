#!/usr/bin/python3
"""base geometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define class"""
    def __init__(self, size):
        """initialize rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
