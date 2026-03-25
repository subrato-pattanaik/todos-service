"""
This file sets up an admin interface for the database using Starlette Admin.
It imports the necessary components, creates the FastAPI app, and mounts the admin interface to it.
This allows you to manage your database records through a web interface.
"""

from fastapi import FastAPI
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from src.models import Todo, Note
from src.database import engine


def setup_admin_interface_for_my_database(app: FastAPI):
    admin = Admin(
        engine,
        title="Admin Panel for my server app",
        base_url="/admin_view",
    )

    # Add a view for the Todo model to the admin interface
    # This will allow you to perform CRUD operations on the Todo records through the admin panel UI.
    admin.add_view(ModelView(Todo))
    admin.add_view(ModelView(Note))
    # add more views for other models if needed

    # Mount the admin interface to the FastAPI app
    admin.mount_to(app)
