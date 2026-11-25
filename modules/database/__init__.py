"""Database layer for CalorieTracker."""

from .db import DB_PATH, get_connection, init_db
from .users import authenticate_user, register_user

__all__ = [
    "DB_PATH",
    "get_connection",
    "init_db",
    "register_user",
    "authenticate_user",
]
