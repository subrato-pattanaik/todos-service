"""DB models for the notes module."""

import uuid
from sqlmodel import Field
from src.notes.schemas import NoteBase
from src.notes.constants import TABLE_NAME


class Note(NoteBase, table=True):
    """SQLModel for the notes table. Inherits fields from NoteBase!"""

    __tablename__ = TABLE_NAME

    # UUID generation directly baked into the Field default_factory natively
    id: str | None = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True
    )
