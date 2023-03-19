#!/usr/bin/python3
"""
a python file that contains the class definition of a State and an instance
Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    class definition of a State that links to the MySQL table states
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True,
                autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship('City', cascade="all, delete", backref="states")
