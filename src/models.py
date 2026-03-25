"""Global models for the application.
This file is used to import all models so that they are registered with SQLModel.metadata,
which is necessary for Alembic's autogenerate feature to work properly.
"""

from sqlmodel import SQLModel

# Set naming convention for auto-generating constraint names
# This is especially crucial for Alembic batch operations in SQLite.
SQLModel.metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Import all models here so that they are registered with SQLModel.metadata.
# This makes it easy for Alembic's env.py to find them.
from src.todos.models import Todo  # noqa: E402
from src.notes.models import Note  # noqa: E402

# Expose them so linters don't complain about unused imports
__all__ = ["SQLModel", "Todo", "Note"]
