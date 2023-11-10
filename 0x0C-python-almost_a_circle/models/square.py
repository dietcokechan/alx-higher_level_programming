#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """override str method"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.size)
