#!/usr/bin/python3
""" Lists all the states from the database 'hbtn_0e_0_usa'. """

import MySQLdb
import sys

""" Connect to MySQL database """
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    """ Set up cursor to navigate database """
    cursor = db.cursor()

    """ SQL Query """
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    """ Display retrieved states """
    for state in states:
        print(state)
    """ Close connections """
    cursor.close()
    db.close()
