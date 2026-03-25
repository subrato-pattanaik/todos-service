"""
Pydantic schemas for the todos module.
It is for defining the structure of data that is sent to and from the API.
"""

from sqlmodel import SQLModel


class TodoBase(SQLModel):
    """Shared properties for all Todo structures."""

    title: str
    description: str | None = None
    completed: bool = False


class TodoCreate(TodoBase):
    """Schema for creating a new todo item."""

    pass


class TodoUpdate(SQLModel):
    """Schema for updating an existing todo item - all fields optional."""

    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TodoResponse(TodoBase):
    """Schema returned to the client."""

    id: str
    note_id: str | None = None
