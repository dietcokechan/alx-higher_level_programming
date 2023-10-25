#!/usr/bin/python3
"""define square class"""


class Square:
    """Square class
    Attributes:
        __size (int): size of square side
    """
    def __init__(self, size):
        """Init a square
        Args:
            size(int): size of square side
        Returns: None
        """
        self.__size = size
