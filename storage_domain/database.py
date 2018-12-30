from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def loadSession():

    engine = create_engine("postgresql://postgres@localhost:5432/memegen")

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
