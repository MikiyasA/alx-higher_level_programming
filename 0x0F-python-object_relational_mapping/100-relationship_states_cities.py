#!/usr/bin/python3
"""
script that creates states and city to database hbtn_e3_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newS = State(name="California")
    newC = City(name="San Francisco")

    newS.cities.append(newC)

    session.add(newS)
    session.add(newC)
    session.commit()
