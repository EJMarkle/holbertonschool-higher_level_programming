#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. """

import MySQLdb
import sys


def filter_states():
    """Filters states from database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=username,
                        passwd=password,
                        db=database)
    database_cursor = db.cursor()
    database_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    rows = database_cursor.fetchall()
    for row in rows:
        print(row)
    database_cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()