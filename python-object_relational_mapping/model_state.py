#!/usr/bin/python3
"""
this is external  
"""

from sqlalchemy  import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """
     this is local
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128),nullable=False)

