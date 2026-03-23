"""Global models for the application.
This file is used to import all models so that they are registered with SQLModel.metadata,
which is necessary for Alembic's autogenerate feature to work properly.
"""

from sqlmodel import SQLModel

# Import all models here so that they are registered with SQLModel.metadata.
# This makes it easy for Alembic's env.py to find them.
from src.todos.models import Todo

# Expose them so linters don't complain about unused imports
__all__ = ["SQLModel", "Todo"]
