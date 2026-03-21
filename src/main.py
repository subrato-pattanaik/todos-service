"""
Run with:
    make dev
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.config import APP_TITLE, APP_VERSION, APP_DESCRIPTION
from src.database import init_db
from src.exceptions import AppException
from src.todos.router import router as todos_router


def create_app() -> FastAPI:
    """FastAPI instance"""
    # Startup/shutdown events
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Everything before the yield runs on startup
        init_db()
        yield
        # Everything after the yield runs on shutdown (nothing to do here)

    app = FastAPI(
        title=APP_TITLE,
        version=APP_VERSION, 
        description=APP_DESCRIPTION,
        lifespan=lifespan,
    )

    # Global and common exception handlers
    @app.exception_handler(AppException)
    async def app_exception_handler(_request: Request, exc: AppException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    # List of Routers
    app.include_router(todos_router)
    # app.include.router(notes_router)
    return app


app = create_app()
