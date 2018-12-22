from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker


def loadSession():

    engine = create_engine("postgresql://postgres@localhost:5432/memegen")

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
