"""DB models for the todos module."""

import uuid
from sqlmodel import Field
from src.todos.schemas import TodoBase
from src.todos.constants import TABLE_NAME


class Todo(TodoBase, table=True):
    """SQLModel for the todos table. Inherits fields from TodoBase!"""

    __tablename__ = TABLE_NAME

    # UUID generation directly baked into the Field default_factory natively
    id: str | None = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True
    )
