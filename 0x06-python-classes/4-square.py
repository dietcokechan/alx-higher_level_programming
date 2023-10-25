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
        self.__size = size

    def area(self):
        """Finds area of square
        Returns: Area
        """
        return self.__size ** 2

    @property
    def size(self):
        """__size getter
        Returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """__size setter
        Args:
            value (int): size of square
        Returns: None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
