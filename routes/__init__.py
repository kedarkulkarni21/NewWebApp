"""
Routes package initialization
"""

from .book_routes import register_book_routes
from .auth_routes import register_auth_routes

__all__ = ['register_book_routes', 'register_auth_routes']