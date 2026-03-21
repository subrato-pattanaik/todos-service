"""Utility functions for the todos module (non-business-logic helpers)."""

import sqlite3

from src.todos.schemas import TodoResponse


def row_to_response(row: sqlite3.Row) -> TodoResponse:
    """Convert a database row to a TodoResponse schema."""
    return TodoResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        completed=bool(row["completed"]),
    )
