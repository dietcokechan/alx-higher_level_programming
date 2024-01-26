#!/usr/bin/python3
""" post an email #1 """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    postrq = requests.post(url, data)
    print(postrq.text)
