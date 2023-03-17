#!/usr/bin/python3
"""
a script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_n = argv[4]
    db_url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}'

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name==state_n).first()

    if result is not None:
        print(f'{result.id}')
    else:
        print('Not found')
