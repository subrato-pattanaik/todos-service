"""
Todo-specific exceptions.
"""

from src.exceptions import AppException


class TodoNotFound(AppException):
    """Raised when a requested todo does not exist."""

    def __init__(self, todo_id: str):
        super().__init__(detail=f"Todo with id '{todo_id}' not found", status_code=404)


class TodoUpdateEmpty(AppException):
    """Raised when an update request contains no fields to update."""

    def __init__(self):
        super().__init__(detail="No fields to update", status_code=400)
