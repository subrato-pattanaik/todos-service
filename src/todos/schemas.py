"""
Pydantic schemas for the todos module.
It is for defining the structure of data that is sent to and from the API.
"""

from pydantic import BaseModel


class TodoCreate(BaseModel):
    """Schema for creating a new todo item."""

    title: str
    description: str
    completed: bool = False


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item - all fields optional."""

    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TodoResponse(BaseModel):
    """Schema returned to the client."""

    id: str
    title: str
    description: str
    completed: bool
