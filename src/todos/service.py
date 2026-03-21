"""Business logic for the todos module."""

import sqlite3
import uuid

from src.todos.exceptions import TodoNotFound, TodoUpdateEmpty
from src.todos.schemas import TodoCreate, TodoResponse, TodoUpdate
from src.todos.utils import row_to_response


def create_todo(conn: sqlite3.Connection, todo: TodoCreate) -> TodoResponse:
    """Create a new todo item and return it."""
    todo_id = str(uuid.uuid4())
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (id, title, description, completed) VALUES (?, ?, ?, ?)",
        (todo_id, todo.title, todo.description, int(todo.completed)),
    )
    conn.commit()
    return TodoResponse(
        id=todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )


def get_all_todos(conn: sqlite3.Connection) -> list[TodoResponse]:
    """Return every todo item in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    rows = cursor.fetchall()
    return [row_to_response(row) for row in rows]


def get_todo_by_id(conn: sqlite3.Connection, todo_id: str) -> TodoResponse:
    """Return a single todo by ID. Raises TodoNotFound if missing."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    if not row:
        raise TodoNotFound(todo_id)
    return row_to_response(row)


def update_todo(
    conn: sqlite3.Connection, todo_id: str, todo: TodoUpdate
) -> TodoResponse:
    """Update an existing todo item. Raises TodoNotFound / TodoUpdateEmpty."""
    cursor = conn.cursor()

    # Verify existence
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise TodoNotFound(todo_id)

    # Build dynamic update
    update_fields: list[str] = []
    values: list[str | int] = []

    if todo.title is not None:
        update_fields.append("title = ?")
        values.append(todo.title)
    if todo.description is not None:
        update_fields.append("description = ?")
        values.append(todo.description)
    if todo.completed is not None:
        update_fields.append("completed = ?")
        values.append(int(todo.completed))

    if not update_fields:
        raise TodoUpdateEmpty()

    values.append(todo_id)
    query = f"UPDATE todos SET {', '.join(update_fields)} WHERE id = ?"
    cursor.execute(query, values)
    conn.commit()

    # Return updated todo
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    return row_to_response(cursor.fetchone())


def delete_todo(conn: sqlite3.Connection, todo_id: str) -> dict[str, str]:
    """Delete a todo by ID. Raises TodoNotFound if missing."""
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise TodoNotFound(todo_id)

    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    return {"message": "Todo deleted successfully"}
