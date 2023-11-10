#!/usr/bin/python3
"""rctangle class"""
from models.base import Base


class Rectangle(Base):
    """class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.__y = value
