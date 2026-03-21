"""Database connection and initialization utilities."""

from sqlmodel import SQLModel, create_engine
from src.config import DATABASE_URL

# sqlite is not thread safe, so we need to pass this flag to avoid the server from crashing
# if multiple threads try to access the database
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)


def init_db() -> None:
    """Initialize the database - create tables if they don't exist."""
    from src.todos import models  # noqa: F401

    SQLModel.metadata.create_all(engine)
