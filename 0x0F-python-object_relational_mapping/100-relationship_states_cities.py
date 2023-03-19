#!/usr/bin/python3
"""
 a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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
    
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.state.append(new_city)

    session.commit()
