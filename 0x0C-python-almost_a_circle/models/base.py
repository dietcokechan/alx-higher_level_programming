#!/usr/bin/python3
"""base class"""
import json
import os.path
import csv


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
        except Exception as e:
            strs = '[]'
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as file:
            file.write(strs)

    @staticmethod
    def from_json_string(json_string):
        """returns dictionary of json string"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set"""
        if cls.__name__ == 'Square':
            ins = cls(1)
        if cls.__name__ == 'Rectangle':
            ins = cls(1, 1)
        if ins:
            ins.update(**dictionary)
            return ins

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as file:
                dicts = cls.from_json_string(file.read())
            return [cls.create(**d) for d in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        try:
            csvs = [i.to_dictionary() for i in list_objs]
        except:
            csvs = '[]'
        keys = csvs[0].keys()
        with open(cls.__name__ + '.csv', 'w') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []
        else:
            with open(cls.__name__ + '.csv', 'r') as file:
                read = csv.DictReader(file)
                csvs = [row for row in read]
                for row in csvs:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except:
                            pass
            return [cls.create(**d) for d in csvs]
