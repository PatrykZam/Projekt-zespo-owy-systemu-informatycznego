"""Tests for user-owned product CRUD operations."""

import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

from modules.database.db import get_connection, init_db
from modules.database.products import (
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)


class ProductCrudTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_products.db"
        init_db(self.db_path)
        with closing(get_connection(self.db_path)) as connection:
            with connection:
                cursor = connection.execute(
                    """
                    INSERT INTO users (username, password_hash)
                    VALUES ('anna', 'test-hash')
                    """
                )
                self.user_id = int(cursor.lastrowid)
                cursor = connection.execute(
                    """
                    INSERT INTO users (username, password_hash)
                    VALUES ('jan', 'test-hash')
                    """
                )
                self.other_user_id = int(cursor.lastrowid)

    def tearDown(self):
        self.temp_dir.cleanup()

    def add_product(self, name="Jabłko", unit="g"):
        return create_product(
            self.user_id, name, unit, 52, 0.3, 0.2, 14, self.db_path
        )

    def test_create_get_and_list_products(self):
        product_id = self.add_product()

        product = get_product(self.user_id, product_id, self.db_path)
        products = list_products(self.user_id, db_path=self.db_path)

        self.assertEqual(product["name"], "Jabłko")
        self.assertEqual(product["reference_unit"], "g")
        self.assertEqual(product["kcal_per_100"], 52.0)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["id"], product_id)

    def test_list_products_filters_by_name_without_matching_other_users(self):
        self.add_product("Sok jabłkowy")
        create_product(
            self.other_user_id, "Sok pomarańczowy", "ml",
            45, 0.7, 0.1, 10, self.db_path
        )

        results = list_products(self.user_id, "jabł", self.db_path)

        self.assertEqual([item["name"] for item in results], ["Sok jabłkowy"])

    def test_search_treats_sql_like_wildcards_as_literal_characters(self):
        self.add_product("100% sok")
        self.add_product("1000 sok")

        results = list_products(self.user_id, "%", self.db_path)

        self.assertEqual([item["name"] for item in results], ["100% sok"])

    def test_update_product_changes_only_supplied_fields(self):
        product_id = self.add_product()

        updated = update_product(
            self.user_id, product_id, name="Gruszka",
            kcal_per_100=57, db_path=self.db_path
        )
        product = get_product(self.user_id, product_id, self.db_path)

        self.assertTrue(updated)
        self.assertEqual(product["name"], "Gruszka")
        self.assertEqual(product["kcal_per_100"], 57.0)
        self.assertEqual(product["protein_g_per_100"], 0.3)

    def test_product_operations_do_not_expose_or_modify_another_users_product(self):
        product_id = self.add_product()

        self.assertIsNone(get_product(self.other_user_id, product_id, self.db_path))
        self.assertFalse(
            update_product(
                self.other_user_id, product_id, name="Zmieniona",
                db_path=self.db_path
            )
        )
        self.assertFalse(
            delete_product(self.other_user_id, product_id, self.db_path)
        )
        self.assertEqual(
            get_product(self.user_id, product_id, self.db_path)["name"], "Jabłko"
        )

    def test_delete_product_preserves_food_entry_snapshot(self):
        product_id = self.add_product()
        with closing(get_connection(self.db_path)) as connection:
            with connection:
                connection.execute(
                    """
                    INSERT INTO food_entries (
                        user_id, product_id, product_name, consumed_on,
                        quantity, unit, kcal, protein_g, fat_g, carbs_g
                    )
                    VALUES (?, ?, 'Jabłko', '2026-11-26', 150, 'g',
                            78, 0.45, 0.3, 21)
                    """,
                    (self.user_id, product_id),
                )

        self.assertTrue(delete_product(self.user_id, product_id, self.db_path))
        self.assertIsNone(get_product(self.user_id, product_id, self.db_path))

        with closing(get_connection(self.db_path)) as connection:
            entry = connection.execute(
                "SELECT product_id, product_name, kcal FROM food_entries"
            ).fetchone()

        self.assertIsNone(entry["product_id"])
        self.assertEqual(entry["product_name"], "Jabłko")
        self.assertEqual(entry["kcal"], 78)

    def test_unit_cannot_be_changed_when_existing_entries_use_other_unit(self):
        product_id = self.add_product("Napój", "ml")
        with closing(get_connection(self.db_path)) as connection:
            with connection:
                connection.execute(
                    """
                    INSERT INTO food_entries (
                        user_id, product_id, product_name, consumed_on,
                        quantity, unit, kcal, protein_g, fat_g, carbs_g
                    )
                    VALUES (?, ?, 'Napój', '2026-11-26', 250, 'ml',
                            100, 1, 0, 24)
                    """,
                    (self.user_id, product_id),
                )

        with self.assertRaisesRegex(ValueError, "niezgodną jednostką"):
            update_product(
                self.user_id, product_id, reference_unit="g",
                db_path=self.db_path
            )

    def test_create_product_rejects_invalid_data(self):
        invalid_products = [
            ("", "g", 10, 1, 1, 1),
            ("Mleko", "kg", 10, 1, 1, 1),
            ("Mleko", "ml", -1, 1, 1, 1),
            ("Mleko", "ml", float("nan"), 1, 1, 1),
            ("Mleko", "ml", 10, float("inf"), 1, 1),
        ]

        for name, unit, kcal, protein, fat, carbs in invalid_products:
            with self.subTest(name=name, unit=unit, kcal=kcal):
                with self.assertRaises(ValueError):
                    create_product(
                        self.user_id, name, unit, kcal, protein, fat, carbs,
                        self.db_path
                    )

    def test_create_product_rejects_unknown_user(self):
        with self.assertRaises(sqlite3.IntegrityError):
            create_product(
                99999, "Produkt", "g", 10, 1, 1, 1, self.db_path
            )

    def test_update_product_requires_at_least_one_field(self):
        product_id = self.add_product()

        with self.assertRaisesRegex(ValueError, "co najmniej jedno pole"):
            update_product(self.user_id, product_id, db_path=self.db_path)

    def test_delete_missing_product_returns_false(self):
        self.assertFalse(delete_product(self.user_id, 99999, self.db_path))


if __name__ == "__main__":
    unittest.main()
