#!/usr/bin/python3
"""
The module that contains the class definition of a City
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ Class State inherit from Base to create db
    using ORM
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
          nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
