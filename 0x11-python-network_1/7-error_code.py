#!/usr/bin/python3
""" error code #1 """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    try:
        print(res.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.code))
