#!/usr/bin/python3
"""import modules and functions"""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

jsonList = load_from_json_file("add_item.json")

for i in sys.argv[1:]:
    jsonList.append(i)
save_to_json_file(jsonList, "add_item.json")
