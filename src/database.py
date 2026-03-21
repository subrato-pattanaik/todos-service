"""Database connection and initialization utilities."""

import sqlite3
from contextlib import contextmanager

from src.config import DATABASE_URL


@contextmanager
def get_db_connection():
    """Context manager that yields a sqlite3 connection and ensures it is closed."""
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # return rows as dict-like objects
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """Initialize the database - create tables if they don't exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0
            )
        """)
        conn.commit()
