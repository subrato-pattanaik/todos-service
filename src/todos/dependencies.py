"""Router dependencies for the todos module."""

import sqlite3
from collections.abc import Generator

from src.config import DATABASE_URL


def get_db() -> Generator[sqlite3.Connection, None, None]:
    """FastAPI dependency that provides a database connection per request."""
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
