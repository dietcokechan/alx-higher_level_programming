#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value for integer and positive"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class rectangle"""


class Rectangle(BaseGeometry):
    """define class"""

    def __init__(self, width, height):
        """initialize rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """return string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
