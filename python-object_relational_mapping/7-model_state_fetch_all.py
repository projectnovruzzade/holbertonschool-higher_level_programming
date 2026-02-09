#!/usr/bin/python3
"""
this is external
"""


import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    this is external
    """
    usm = sys.argv[1]
    pwd = sys.argv[2]
    dbnm = sys.argv[3]

    engine = create_engine(
        f"mysql+pymysql://{usm}:{pwd}@localhost:3306/{dbnm}?charset=utf8mb4",
        echo=True,
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = select(State).group_by(State.id)
    result = session.execute(stmt)
    datas = result.scalars().all()

    for data in datas:
        print("{}: {}".format(data.id, data.name))
