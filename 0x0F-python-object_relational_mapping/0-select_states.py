#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost", user=user, password=passwd,
                         database=db_name)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    q = cur.fetchall()
    for i in q:
        print(i)
