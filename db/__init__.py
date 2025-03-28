"""
Database package initialization
"""

from .database import get_db_client

# Export get_db_client function
__all__ = ['get_db_client']