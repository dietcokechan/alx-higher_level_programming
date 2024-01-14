#!/usr/bin/python3
"""
script that lists all states f with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for i in rows:
        if i[1][0] == 'N':
            print(i)
    cursor.close()
    db.close()
