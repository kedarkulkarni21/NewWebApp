"""
Views package initialization
"""

from .components import footer
from .book_views import render_book, render_book_list, render_book_form, render_main_content
from .auth_views import render_signup_form

__all__ = [
    'footer', 
    'render_book', 
    'render_book_list', 
    'render_book_form', 
    'render_main_content',
    'render_signup_form'
]