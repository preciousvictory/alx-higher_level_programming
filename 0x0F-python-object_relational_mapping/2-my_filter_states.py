#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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
    cur.execute("""SELECT * FROM states WHERE BINARY name = %s""", [state])
    q = cur.fetchall()
    for i in q:
        print(i)
