"""
Pydantic schemas for the notes module.
It is for defining the structure of data that is sent to and from the API.
"""

from sqlmodel import SQLModel


class NoteBase(SQLModel):
    """Shared properties for all Note structures."""

    title: str
    content: str | None = None


class NoteCreate(NoteBase):
    """Schema for creating a new note item."""

    pass


class NoteUpdate(SQLModel):
    """Schema for updating an existing note item - all fields optional."""

    title: str | None = None
    content: str | None = None


class NoteResponse(NoteBase):
    """Schema returned to the client."""

    id: str
