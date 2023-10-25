#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. """

import MySQLdb
import sys

def filter_states():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
    )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states()