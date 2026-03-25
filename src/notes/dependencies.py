"""Router dependencies for the notes module."""

from collections.abc import Generator
from sqlmodel import Session
from src.database import engine


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database connection per request."""
    with Session(engine) as session:
        yield session
