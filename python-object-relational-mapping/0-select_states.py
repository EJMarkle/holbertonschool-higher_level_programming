#!/usr/bin/python3
""" Lists all 'states' from the database hbtn_0e_0_usa and displays them. """

import MySQLdb
import sys

""" Check for correct amount of arguments """
if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password> <database_name>")
    sys.exit(1)

""" Assign arguments to variables """
username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

""" Connect to MySQL server """
try:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
    )

    """ Create cursor to navigate database """
    cursor = db.cursor()

    """  SQL query to find the states """
    cursor.execute("SELECT * FROM states ORDER BY id")

    """ Fetch all results """
    states = cursor.fetchall()

    """ Display results """
    for state in states:
        print(state)

except MySQLdb.Error as err:
    print("Error:", err)

""" Close connections """
finally:
    cursor.close()
    db.close()