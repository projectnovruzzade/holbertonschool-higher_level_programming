#!/usr/bin/python3
"""
this is global enviroment
"""


import sys
import MySQLdb

if __name__ == "__main__":
    """
        this is local enviroment
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state, ))

    states = cursor.fetchall()
    l = len(states)
    c = 0
    for k in range(l):
        c += 1
        if c == l:
            print(states[k][0], end="\n")
        else:
            print(states[k][0], end=", ")

    cursor.close()
    db.close()
