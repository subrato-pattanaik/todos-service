"""Global application configuration."""

import os


# Database
DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///todos.db")

# Application
APP_TITLE: str = "Todos Service"
APP_VERSION: str = "0.1.0"
APP_DESCRIPTION: str = "A simple todo management API built with FastAPI."
