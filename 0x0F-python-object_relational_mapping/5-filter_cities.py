#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state = argv[4]
    db = MySQLdb.connect(host="localhost", user=user, password=passwd,
                         database=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id\
                =cities.state_id WHERE BINARY states.name = %s ORDER BY\
                cities.id ASC", (state,))
    q = cur.fetchall()
    for i in range(len(q)):
        print(q[i][0], end='')
        if i != len(q) - 1:
            print(', ', end='')
    print()
