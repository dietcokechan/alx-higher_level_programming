#!/usr/bin/python3
"""import json module"""
import json


def load_from_json_file(filename):
    """loads an object from json file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))
