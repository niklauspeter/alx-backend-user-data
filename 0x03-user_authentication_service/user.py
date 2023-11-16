#!/usr/bin/python3
"""
User class modeled to represent
user table in DB
"""
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()


class User(Base):
    """User class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """
        String Rep
        """
        return f"User: id={self.id}"
