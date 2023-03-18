#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all City objects from the
database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    result = session.query(State.name, City.id, City.name)\
                           .join(City, City.state_id == State.id)\
                           .order_by(City.id)

    for row in result:
        print(f'{row[0]}: ({row[1]}) {row[2]}')
