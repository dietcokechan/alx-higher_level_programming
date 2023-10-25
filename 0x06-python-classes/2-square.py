#!/usr/bin/python3
"""define square class"""


class Square:
    """Square class
    Attributes:
        __size (int): size of square side
    """
    def __init__(self, size=0):
        """Init a square
        Args:
            size(int): size of square side
        Returns: None
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
