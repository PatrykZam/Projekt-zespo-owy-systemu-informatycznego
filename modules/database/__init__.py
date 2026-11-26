"""Database layer for CalorieTracker."""

from .db import DB_PATH, get_connection, init_db
from .users import authenticate_user, register_user
from .products import create_product, get_product, list_products, update_product, delete_product

__all__ = [
    "DB_PATH",
    "get_connection",
    "init_db",
    "register_user",
    "authenticate_user",
    "create_product",
    "get_product",
    "list_products",
    "update_product",
    "delete_product",
]
