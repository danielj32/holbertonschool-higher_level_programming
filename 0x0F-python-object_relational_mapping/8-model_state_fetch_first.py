#!/usr/bin/python3
"""script that prints the first
State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
if __name__ == "__main__":
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2],
                               sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(en)
    session = Session(en)
    state1 = session.query(State).order_by(State.id).first()
    if state1:
        print("{}: {}".format(state1.id, state1.name))
    else:
        print("Nothing")
    session.close()
