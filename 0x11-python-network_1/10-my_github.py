#!/usr/bin/python3
""" my github """
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/search/repositories?q=github+api', auth=auth)
    print(res.json().get("id"))
