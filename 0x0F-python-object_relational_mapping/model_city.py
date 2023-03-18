#!/usr/bin/python3
"""
contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
     class definition of City that links to the MySQL table cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True,
                autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
