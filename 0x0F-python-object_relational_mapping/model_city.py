#!/usr/bin/python3
"""
The module that contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Class City inherit from Base to create db
    using ORM
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
          nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
