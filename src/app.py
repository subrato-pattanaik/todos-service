"""
Main FastAPI application setup with structured logging and lifecycle management.
Keeping this separate from main.py allows for better organization and easier testing.
"""

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.logging_config import configure_logging, get_logger
from src.config import APP_TITLE, APP_VERSION, APP_DESCRIPTION
from src.database import init_db
from src.exceptions import AppException
from src.todos.router import router as todos_router
from src.notes.router import router as notes_router


configure_logging()
logger = get_logger(__name__)


def create_app() -> FastAPI:
    """FastAPI instance"""

    # Startup/shutdown events
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info("server_startup")
        init_db()  # Initialize the database on startup
        yield  # Pauses the execution of the function and the server starts running.
        # The server is now running and waiting for HTTP requests
        # Everything after the yield runs on shutdown (nothing to do here)
        # It is mainly used for closing database connections, cleaning up resources, etc when shutting down.
        logger.info("server_shutdown")

    main_server_app = FastAPI(
        title=APP_TITLE,
        version=APP_VERSION,
        description=APP_DESCRIPTION,
        lifespan=lifespan,
    )

    # Logging Middleware (using structlog for structured analytics)
    @main_server_app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = (time.perf_counter() - start_time) * 1000

        # Log request details in a structured format (perfect for analytics)
        logger.info(
            "request_processed",
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration_ms=round(process_time, 2),
            ip=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent"),
        )
        return response

    # Global and common exception handlers
    @main_server_app.exception_handler(AppException)
    async def app_exception_handler(_request: Request, exc: AppException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    # List of Routers
    main_server_app.include_router(todos_router)
    main_server_app.include_router(notes_router)
    return main_server_app
