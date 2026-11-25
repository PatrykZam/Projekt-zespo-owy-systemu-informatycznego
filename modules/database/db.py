"""SQLite connection and schema initialization for CalorieTracker."""

import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Optional, Union


DB_PATH = Path(__file__).resolve().parents[2] / "calorietracker.db"
DatabasePath = Union[str, Path]


_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL COLLATE NOCASE UNIQUE
        CHECK (length(trim(username)) > 0),
    password_hash TEXT NOT NULL
        CHECK (length(trim(password_hash)) > 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL CHECK (length(trim(name)) > 0),
    reference_unit TEXT NOT NULL CHECK (reference_unit IN ('g', 'ml')),
    kcal_per_100 REAL NOT NULL CHECK (kcal_per_100 >= 0),
    protein_g_per_100 REAL NOT NULL CHECK (protein_g_per_100 >= 0),
    fat_g_per_100 REAL NOT NULL CHECK (fat_g_per_100 >= 0),
    carbs_g_per_100 REAL NOT NULL CHECK (carbs_g_per_100 >= 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE (id, user_id)
);

CREATE TABLE IF NOT EXISTS food_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER,
    product_name TEXT NOT NULL CHECK (length(trim(product_name)) > 0),
    consumed_on TEXT NOT NULL
        CHECK (length(consumed_on) = 10 AND date(consumed_on) IS NOT NULL),
    quantity REAL NOT NULL CHECK (quantity > 0),
    unit TEXT NOT NULL CHECK (unit IN ('g', 'kg', 'ml', 'l')),
    kcal REAL NOT NULL CHECK (kcal >= 0),
    protein_g REAL NOT NULL CHECK (protein_g >= 0),
    fat_g REAL NOT NULL CHECK (fat_g >= 0),
    carbs_g REAL NOT NULL CHECK (carbs_g >= 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS daily_goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    calories REAL NOT NULL CHECK (calories >= 0),
    protein_g REAL NOT NULL CHECK (protein_g >= 0),
    fat_g REAL NOT NULL CHECK (fat_g >= 0),
    carbs_g REAL NOT NULL CHECK (carbs_g >= 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_products_user_name
    ON products(user_id, name);

CREATE INDEX IF NOT EXISTS idx_food_entries_user_date
    ON food_entries(user_id, consumed_on);

CREATE INDEX IF NOT EXISTS idx_food_entries_product
    ON food_entries(product_id);

CREATE TRIGGER IF NOT EXISTS trg_food_entry_product_owner_insert
BEFORE INSERT ON food_entries
WHEN NEW.product_id IS NOT NULL
 AND NOT EXISTS (
     SELECT 1 FROM products
     WHERE id = NEW.product_id AND user_id = NEW.user_id
 )
BEGIN
    SELECT RAISE(ABORT, 'product does not belong to this user');
END;

CREATE TRIGGER IF NOT EXISTS trg_food_entry_product_owner_update
BEFORE UPDATE OF product_id, user_id ON food_entries
WHEN NEW.product_id IS NOT NULL
 AND NOT EXISTS (
     SELECT 1 FROM products
     WHERE id = NEW.product_id AND user_id = NEW.user_id
 )
BEGIN
    SELECT RAISE(ABORT, 'product does not belong to this user');
END;

CREATE TRIGGER IF NOT EXISTS trg_food_entry_unit_insert
BEFORE INSERT ON food_entries
WHEN NEW.product_id IS NOT NULL
 AND NOT EXISTS (
     SELECT 1 FROM products
     WHERE id = NEW.product_id
       AND ((reference_unit = 'g' AND NEW.unit IN ('g', 'kg'))
         OR (reference_unit = 'ml' AND NEW.unit IN ('ml', 'l')))
 )
BEGIN
    SELECT RAISE(ABORT, 'food entry unit is incompatible with product reference unit');
END;

CREATE TRIGGER IF NOT EXISTS trg_food_entry_unit_update
BEFORE UPDATE OF product_id, unit ON food_entries
WHEN NEW.product_id IS NOT NULL
 AND NOT EXISTS (
     SELECT 1 FROM products
     WHERE id = NEW.product_id
       AND ((reference_unit = 'g' AND NEW.unit IN ('g', 'kg'))
         OR (reference_unit = 'ml' AND NEW.unit IN ('ml', 'l')))
 )
BEGIN
    SELECT RAISE(ABORT, 'food entry unit is incompatible with product reference unit');
END;
"""


def _resolve_db_path(db_path: Optional[DatabasePath]) -> str:
    """Return a SQLite-compatible path; memory databases are supported for tests."""
    if db_path is None:
        return str(DB_PATH)
    return str(db_path)


def get_connection(db_path: Optional[DatabasePath] = None) -> sqlite3.Connection:
    """Open a configured SQLite connection with foreign-key checks enabled."""
    path = _resolve_db_path(db_path)
    if path != ":memory:":
        Path(path).expanduser().parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 10000")
    return connection


def init_db(db_path: Optional[DatabasePath] = None) -> None:
    """Create the database tables, indexes and integrity triggers if missing."""
    with closing(get_connection(db_path)) as connection:
        connection.executescript(_SCHEMA)
        connection.execute("PRAGMA user_version = 1")
        connection.commit()
