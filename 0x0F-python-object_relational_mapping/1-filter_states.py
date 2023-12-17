#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    mycur = db.cursor()
    mycur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = mycur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    mycur.close()
    db.close()
