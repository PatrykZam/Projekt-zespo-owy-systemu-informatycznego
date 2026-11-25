"""Tests for CalorieTracker user registration and authentication."""

import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

from modules.database.db import get_connection, init_db
from modules.database.users import authenticate_user, register_user


class UserAuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_users.db"
        init_db(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_register_user_stores_a_hash_and_returns_id(self):
        user_id = register_user("  jan  ", "tajne-haslo", self.db_path)

        self.assertGreater(user_id, 0)
        with closing(get_connection(self.db_path)) as connection:
            row = connection.execute(
                "SELECT id, username, password_hash FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()

        self.assertEqual(row["username"], "jan")
        self.assertNotEqual(row["password_hash"], "tajne-haslo")
        self.assertTrue(row["password_hash"].startswith("pbkdf2_sha256$"))

    def test_duplicate_username_is_rejected_without_case_sensitivity(self):
        register_user("Patryk", "haslo-1", self.db_path)

        with self.assertRaisesRegex(ValueError, "już zajęta"):
            register_user("patryk", "haslo-2", self.db_path)

    def test_authenticate_user_returns_public_user_data(self):
        user_id = register_user("anna", "bezpieczne-haslo", self.db_path)

        user = authenticate_user("ANNA", "bezpieczne-haslo", self.db_path)

        self.assertEqual(user, {"id": user_id, "username": "anna"})
        self.assertNotIn("password_hash", user)

    def test_wrong_password_is_rejected(self):
        register_user("anna", "poprawne-haslo", self.db_path)

        self.assertIsNone(
            authenticate_user("anna", "niepoprawne-haslo", self.db_path)
        )

    def test_unknown_username_is_rejected(self):
        self.assertIsNone(
            authenticate_user("nie-ma-takiego", "dowolne-haslo", self.db_path)
        )

    def test_empty_username_or_password_cannot_be_registered(self):
        with self.assertRaises(ValueError):
            register_user("   ", "haslo", self.db_path)
        with self.assertRaises(ValueError):
            register_user("jan", "", self.db_path)

        with closing(get_connection(self.db_path)) as connection:
            count = connection.execute(
                "SELECT COUNT(*) AS total FROM users"
            ).fetchone()["total"]

        self.assertEqual(count, 0)

    def test_malformed_stored_hash_fails_authentication(self):
        register_user("jan", "haslo", self.db_path)
        with closing(get_connection(self.db_path)) as connection:
            with connection:
                connection.execute(
                    "UPDATE users SET password_hash = ? WHERE username = ?",
                    ("not-a-valid-hash", "jan"),
                )

        self.assertIsNone(authenticate_user("jan", "haslo", self.db_path))


if __name__ == "__main__":
    unittest.main()
