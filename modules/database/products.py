"""CRUD operations for user-owned products in CalorieTracker."""

import math
import sqlite3
from contextlib import closing
from typing import Optional

from .db import DatabasePath, get_connection


def _validate_id(value: int, field_name: str) -> int:
    """Validate a positive integer database identifier."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} musi być dodatnią liczbą całkowitą.")
    return value


def _validate_name(name: str) -> str:
    """Normalize a non-empty product name."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Nazwa produktu nie może być pusta.")
    return name.strip()


def _validate_unit(reference_unit: str) -> str:
    """Normalize the product reference unit."""
    if not isinstance(reference_unit, str):
        raise ValueError("Jednostka produktu musi mieć wartość 'g' lub 'ml'.")
    unit = reference_unit.strip().lower()
    if unit not in ("g", "ml"):
        raise ValueError("Jednostka produktu musi mieć wartość 'g' lub 'ml'.")
    return unit


def _validate_nutrient(value: float, field_name: str) -> float:
    """Validate a non-negative finite nutritional value."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"Wartość '{field_name}' musi być liczbą.")
    numeric_value = float(value)
    if not math.isfinite(numeric_value) or numeric_value < 0:
        raise ValueError(f"Wartość '{field_name}' musi być nieujemną liczbą.")
    return numeric_value


def _product_to_dict(row: sqlite3.Row) -> dict:
    """Convert a SQLite row into a plain dictionary."""
    return {
        "id": int(row["id"]),
        "user_id": int(row["user_id"]),
        "name": row["name"],
        "reference_unit": row["reference_unit"],
        "kcal_per_100": float(row["kcal_per_100"]),
        "protein_g_per_100": float(row["protein_g_per_100"]),
        "fat_g_per_100": float(row["fat_g_per_100"]),
        "carbs_g_per_100": float(row["carbs_g_per_100"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def create_product(
    user_id: int,
    name: str,
    reference_unit: str,
    kcal_per_100: float,
    protein_g_per_100: float,
    fat_g_per_100: float,
    carbs_g_per_100: float,
    db_path: Optional[DatabasePath] = None,
) -> int:
    """Create a product for a user and return its new ID.

    Nutritional values describe 100 g or 100 ml, according to reference_unit.
    The database must have been initialized with init_db() first.
    """
    user_id = _validate_id(user_id, "user_id")
    normalized_name = _validate_name(name)
    normalized_unit = _validate_unit(reference_unit)
    nutrients = (
        _validate_nutrient(kcal_per_100, "kcal_per_100"),
        _validate_nutrient(protein_g_per_100, "protein_g_per_100"),
        _validate_nutrient(fat_g_per_100, "fat_g_per_100"),
        _validate_nutrient(carbs_g_per_100, "carbs_g_per_100"),
    )

    with closing(get_connection(db_path)) as connection:
        with connection:
            cursor = connection.execute(
                """
                INSERT INTO products (
                    user_id, name, reference_unit, kcal_per_100,
                    protein_g_per_100, fat_g_per_100, carbs_g_per_100
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, normalized_name, normalized_unit, *nutrients),
            )
            return int(cursor.lastrowid)


def get_product(
    user_id: int,
    product_id: int,
    db_path: Optional[DatabasePath] = None,
) -> Optional[dict]:
    """Return one product owned by the user, or None when it is not found."""
    user_id = _validate_id(user_id, "user_id")
    product_id = _validate_id(product_id, "product_id")

    with closing(get_connection(db_path)) as connection:
        row = connection.execute(
            """
            SELECT *
            FROM products
            WHERE id = ? AND user_id = ?
            """,
            (product_id, user_id),
        ).fetchone()

    return _product_to_dict(row) if row is not None else None


def list_products(
    user_id: int,
    search: Optional[str] = None,
    db_path: Optional[DatabasePath] = None,
) -> list:
    """Return a user's products ordered by name, optionally filtered by name."""
    user_id = _validate_id(user_id, "user_id")
    if search is not None and not isinstance(search, str):
        raise ValueError("Fraza wyszukiwania musi być tekstem.")

    with closing(get_connection(db_path)) as connection:
        if search and search.strip():
            rows = connection.execute(
                """
                SELECT *
                FROM products
                WHERE user_id = ? AND name LIKE ? ESCAPE '\'
                ORDER BY name COLLATE NOCASE, id
                """,
                (user_id, "%" + search.strip().replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"),
            ).fetchall()
        else:
            rows = connection.execute(
                """
                SELECT *
                FROM products
                WHERE user_id = ?
                ORDER BY name COLLATE NOCASE, id
                """,
                (user_id,),
            ).fetchall()

    return [_product_to_dict(row) for row in rows]


def update_product(
    user_id: int,
    product_id: int,
    *,
    name: Optional[str] = None,
    reference_unit: Optional[str] = None,
    kcal_per_100: Optional[float] = None,
    protein_g_per_100: Optional[float] = None,
    fat_g_per_100: Optional[float] = None,
    carbs_g_per_100: Optional[float] = None,
    db_path: Optional[DatabasePath] = None,
) -> bool:
    """Update supplied fields of a user's product.

    Returns False when the product does not belong to the user or does not
    exist. At least one field must be supplied.
    """
    user_id = _validate_id(user_id, "user_id")
    product_id = _validate_id(product_id, "product_id")

    values = {}
    if name is not None:
        values["name"] = _validate_name(name)
    if reference_unit is not None:
        values["reference_unit"] = _validate_unit(reference_unit)
    for field_name, value in (
        ("kcal_per_100", kcal_per_100),
        ("protein_g_per_100", protein_g_per_100),
        ("fat_g_per_100", fat_g_per_100),
        ("carbs_g_per_100", carbs_g_per_100),
    ):
        if value is not None:
            values[field_name] = _validate_nutrient(value, field_name)

    if not values:
        raise ValueError("Należy podać co najmniej jedno pole do aktualizacji.")

    assignments = ", ".join(f"{column} = ?" for column in values)
    parameters = list(values.values()) + [product_id, user_id]

    with closing(get_connection(db_path)) as connection:
        with connection:
            if "reference_unit" in values:
                allowed_units = ("g", "kg") if values["reference_unit"] == "g" else ("ml", "l")
                placeholders = ", ".join("?" for _ in allowed_units)
                incompatible_entries = connection.execute(
                    f"""
                    SELECT COUNT(*) AS total
                    FROM food_entries
                    WHERE product_id = ? AND user_id = ?
                      AND unit NOT IN ({placeholders})
                    """,
                    (product_id, user_id, *allowed_units),
                ).fetchone()["total"]
                if incompatible_entries:
                    raise ValueError(
                        "Nie można zmienić jednostki produktu, ponieważ istnieją "
                        "wpisy dziennika z niezgodną jednostką."
                    )

            cursor = connection.execute(
                f"""
                UPDATE products
                SET {assignments}, updated_at = CURRENT_TIMESTAMP
                WHERE id = ? AND user_id = ?
                """,
                parameters,
            )
            return cursor.rowcount > 0


def delete_product(
    user_id: int,
    product_id: int,
    db_path: Optional[DatabasePath] = None,
) -> bool:
    """Delete a product owned by the user.

    Existing food entries keep their nutritional snapshots; the schema sets
    their product_id to NULL when the linked product is deleted.
    """
    user_id = _validate_id(user_id, "user_id")
    product_id = _validate_id(product_id, "product_id")

    with closing(get_connection(db_path)) as connection:
        with connection:
            cursor = connection.execute(
                "DELETE FROM products WHERE id = ? AND user_id = ?",
                (product_id, user_id),
            )
            return cursor.rowcount > 0
