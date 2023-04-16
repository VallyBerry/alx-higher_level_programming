#!/usr/bin/python3
"""
Function to list all State objects from the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    a = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    b = sessionmaker(bind=engine)
    session = b()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
