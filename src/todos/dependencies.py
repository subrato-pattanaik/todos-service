"""Router dependencies for the todos module."""

from collections.abc import Generator
from sqlmodel import Session
from src.database import engine


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database connection per request."""
    # SQLModel allows you to just instantiate Session with the engine directly!
    with Session(engine) as session:
        yield session
