#!/usr/bin/python3
""" response header value #1 """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(dict(res.headers).get("X-Request-Id"))
