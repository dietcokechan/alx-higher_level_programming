#!/usr/bin/python3
"""base class"""
import json


class Base:
    """class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string to a file"""
        try:
            strs = cls.to_json_string([i.to_dictionary() for i in list_objs])
        except:
            strs = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as file:
            file.write(strs)
