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
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.validate("y", value)
        self.__y = value

    def validate(self, input, value):
        """validate input"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(input))
        if (input == 'width' or input == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(input))
        if (input == 'x' or input == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(input))

    def area(self):
        """get area of rectangle"""
        return self.width * self.height

    def display(self):
        """displays rectangle"""
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
                      for i in range(self.height)), end="")

    def __str__(self):
        """override str method"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        """assign arguments to attributes"""
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kwargs:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)
