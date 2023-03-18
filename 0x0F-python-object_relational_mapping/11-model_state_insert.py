#!/usr/bin/python3
"""
a script that adds theState object “Louisiana”to thedatabase hbtn_0e_6_usa
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
    db_url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}'

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    q = session.query(State).filter(State.name == "Louisiana").first()

    print(q)
