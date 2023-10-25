#!/usr/bin/python3
"""define square class"""


class Square:
    """Square class
    Attributes:
        __size (int): size of square side
        __position (tuple): position of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init a square
        Args:
            size(int): size of square side
        Returns: None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """__position getter
        Returns: position of square
        """
        return self.__position

    @position.getter
    def position(self, value):
        """__position setter
        Args:
            value (tuple): position
        Returns: None
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Finds area of square
        Returns: Area
        """
        return self.__size ** 2

    def my_print(self):
        """Print square with #'s
        Returns: None
        """
        if self.__size == 0:
            print()
            return

        if (self.__position[1] > 0):
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
