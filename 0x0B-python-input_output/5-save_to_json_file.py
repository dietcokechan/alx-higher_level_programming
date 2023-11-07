#!/usr/bin/python3
"""import json module"""
import json


def save_to_json_file(my_obj, filename):
    """saves object as json string dump"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
