"""Tests for the initial CalorieTracker SQLite schema."""

import sqlite3
import tempfile
import unittest
from pathlib import Path

from modules.database.db import get_connection, init_db


class DatabaseSchemaTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_calorietracker.db"
        init_db(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initialization_creates_all_required_tables(self):
        with get_connection(self.db_path) as connection:
            rows = connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
            tables = {row["name"] for row in rows}

        self.assertTrue(
            {"users", "products", "food_entries", "daily_goals"}.issubset(tables)
        )

    def test_username_is_unique_case_insensitively(self):
        with get_connection(self.db_path) as connection:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("Patryk", "hash-1"),
            )
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    ("patryk", "hash-2"),
                )

    def test_foreign_keys_and_nutritional_checks_are_enforced(self):
        with get_connection(self.db_path) as connection:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("user1", "hash"),
            )
            user_id = connection.execute(
                "SELECT id FROM users WHERE username = ?", ("user1",)
            ).fetchone()["id"]

            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    """INSERT INTO products
                       (user_id, name, reference_unit, kcal_per_100,
                        protein_g_per_100, fat_g_per_100, carbs_g_per_100)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (user_id, "Bad product", "g", -1, 1, 1, 1),
                )

            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    """INSERT INTO daily_goals
                       (user_id, calories, protein_g, fat_g, carbs_g)
                       VALUES (?, ?, ?, ?, ?)""",
                    (9999, 2000, 100, 70, 200),
                )

    def test_food_entry_keeps_history_when_product_is_deleted(self):
        with get_connection(self.db_path) as connection:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("user1", "hash"),
            )
            user_id = connection.execute(
                "SELECT id FROM users WHERE username = ?", ("user1",)
            ).fetchone()["id"]
            product_id = connection.execute(
                """INSERT INTO products
                   (user_id, name, reference_unit, kcal_per_100,
                    protein_g_per_100, fat_g_per_100, carbs_g_per_100)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (user_id, "Skyr", "ml", 70, 8, 0.2, 4),
            ).lastrowid
            connection.execute(
                """INSERT INTO food_entries
                   (user_id, product_id, product_name, consumed_on, quantity, unit,
                    kcal, protein_g, fat_g, carbs_g)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (user_id, product_id, "Skyr", "2026-11-25", 500, "ml", 350, 40, 1, 20),
            )
            connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
            entry = connection.execute(
                "SELECT product_id, product_name, kcal FROM food_entries"
            ).fetchone()

        self.assertIsNone(entry["product_id"])
        self.assertEqual(entry["product_name"], "Skyr")
        self.assertEqual(entry["kcal"], 350)

    def test_food_entry_cannot_use_another_users_product(self):
        with get_connection(self.db_path) as connection:
            connection.executemany(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                [("user1", "hash"), ("user2", "hash")],
            )
            users = connection.execute("SELECT id FROM users ORDER BY id").fetchall()
            owner_id, other_id = users[0]["id"], users[1]["id"]
            product_id = connection.execute(
                """INSERT INTO products
                   (user_id, name, reference_unit, kcal_per_100,
                    protein_g_per_100, fat_g_per_100, carbs_g_per_100)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (owner_id, "Oats", "g", 370, 13, 7, 60),
            ).lastrowid

            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    """INSERT INTO food_entries
                       (user_id, product_id, product_name, consumed_on, quantity, unit,
                        kcal, protein_g, fat_g, carbs_g)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (other_id, product_id, "Oats", "2026-11-25", 50, "g", 185, 6.5, 3.5, 30),
                )


if __name__ == "__main__":
    unittest.main()
