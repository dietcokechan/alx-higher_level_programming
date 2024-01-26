#!/usr/bin/python3
""" post an email #0 """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    var = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(var).encode("ascii")
    req = urllib.request.Request(url, var)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
