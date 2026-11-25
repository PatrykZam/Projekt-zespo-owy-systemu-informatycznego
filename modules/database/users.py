"""User registration and authentication for CalorieTracker."""

import hashlib
import hmac
import secrets
import sqlite3
from contextlib import closing
from typing import Optional

from .db import DatabasePath, get_connection


_PASSWORD_HASH_ALGORITHM = "pbkdf2_sha256"
_PASSWORD_HASH_ITERATIONS = 600_000
_PASSWORD_SALT_BYTES = 16


def _hash_password(password: str) -> str:
    """Create a salted PBKDF2-HMAC-SHA256 password hash."""
    salt = secrets.token_bytes(_PASSWORD_SALT_BYTES)
    password_bytes = password.encode("utf-8")
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt,
        _PASSWORD_HASH_ITERATIONS,
    )
    return "$".join(
        (
            _PASSWORD_HASH_ALGORITHM,
            str(_PASSWORD_HASH_ITERATIONS),
            salt.hex(),
            digest.hex(),
        )
    )


def _verify_password(password: str, encoded_hash: str) -> bool:
    """Verify a password hash without exposing timing-sensitive comparisons."""
    try:
        algorithm, iterations_text, salt_hex, digest_hex = encoded_hash.split("$")
        if algorithm != _PASSWORD_HASH_ALGORITHM:
            return False

        iterations = int(iterations_text)
        # Reject malformed values and unreasonable work factors from stored data.
        if not 100_000 <= iterations <= 2_000_000:
            return False

        salt = bytes.fromhex(salt_hex)
        expected_digest = bytes.fromhex(digest_hex)
        if len(salt) != _PASSWORD_SALT_BYTES or len(expected_digest) != 32:
            return False

        actual_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations,
        )
        return hmac.compare_digest(actual_digest, expected_digest)
    except (AttributeError, TypeError, ValueError):
        return False


def register_user(
    username: str,
    password: str,
    db_path: Optional[DatabasePath] = None,
) -> int:
    """Register a user and return the new user ID.

    The username is trimmed and is unique without regard to letter case.
    Raises ValueError for empty input or an already registered username.
    The database schema must have been initialized with init_db() first.
    """
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Nazwa użytkownika nie może być pusta.")
    if not isinstance(password, str) or password == "":
        raise ValueError("Hasło nie może być puste.")

    normalized_username = username.strip()
    password_hash = _hash_password(password)

    try:
        with closing(get_connection(db_path)) as connection:
            with connection:
                cursor = connection.execute(
                    """
                    INSERT INTO users (username, password_hash)
                    VALUES (?, ?)
                    """,
                    (normalized_username, password_hash),
                )
                return int(cursor.lastrowid)
    except sqlite3.IntegrityError as error:
        if "UNIQUE constraint failed: users.username" in str(error):
            raise ValueError("Podana nazwa użytkownika jest już zajęta.") from error
        raise


def authenticate_user(
    username: str,
    password: str,
    db_path: Optional[DatabasePath] = None,
) -> Optional[dict]:
    """Return a user's public ID and username for valid credentials.

    Returns None when the username or password is incorrect. Password hashes
    are never included in the returned user data.
    """
    if not isinstance(username, str) or not username.strip():
        return None
    if not isinstance(password, str) or password == "":
        return None

    with closing(get_connection(db_path)) as connection:
        row = connection.execute(
            """
            SELECT id, username, password_hash
            FROM users
            WHERE username = ?
            """,
            (username.strip(),),
        ).fetchone()

    if row is None or not _verify_password(password, row["password_hash"]):
        return None

    return {
        "id": int(row["id"]),
        "username": row["username"],
    }
