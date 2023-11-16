from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import TypeVar


def _hash_password(password: str) -> str:
    """
    _hash_password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
