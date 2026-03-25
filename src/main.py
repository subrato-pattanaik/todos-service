"""
Run with:
    make dev
"""

from src.app import create_app
from src.admin_view_database import setup_admin_interface_for_my_database

# Create the FastAPI app instance
app = create_app()

setup_admin_interface_for_my_database(app)
