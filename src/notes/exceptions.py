"""
Note-specific exceptions.
"""

from src.exceptions import AppException


class NoteNotFound(AppException):
    """Raised when a requested note does not exist."""

    def __init__(self, note_id: str):
        super().__init__(detail=f"Note with id '{note_id}' not found", status_code=404)


class NoteUpdateEmpty(AppException):
    """Raised when an update request contains no fields to update."""

    def __init__(self):
        super().__init__(detail="No fields to update", status_code=400)
