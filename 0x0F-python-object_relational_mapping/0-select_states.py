#!/usr/bin/python3
""" 0-select_states module. This module lists all states from the database
hbtn_0e_0_usa. """

import MySQLdb
from sys import argv

def liststates():
    """ Lists all states from the database hbtn_0e_0_usa. """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    liststates()