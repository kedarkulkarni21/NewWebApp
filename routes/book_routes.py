"""
Book-related route handlers
"""

from fasthtml.common import Titled
from config import DB_TABLE_BOOKS
from views.book_views import render_main_content, render_book_list

def register_book_routes(rt, db_client):
    """Register all book-related routes.
    
    Args:
        rt: Route handler from the FastHTML app
        db_client: Initialized database client
    """
    
    def get_books():
        """Get all books from the database.
        
        Returns:
            list: List of book data dictionaries
        """
        response = db_client.table(DB_TABLE_BOOKS).select("*").order("id", desc=True).execute()
        return response.data
    
    def add_book(book_name, book_author, book_genre):
        """Add a new book to the database.
        
        Args:
            book_name (str): The title of the book
            book_author (str): The author of the book
            book_genre (str): The genre of the book
        """
        db_client.table(DB_TABLE_BOOKS).insert(
            {
                "book_name": book_name,
                "book_author": book_author,
                "book_genre": book_genre,
            }
        ).execute()
    
    @rt('/')
    def home(): 
        """Handle main page requests.
        
        Returns:
            str: HTML for main page
        """
        return Titled("My Library📚", render_main_content(get_books))

    @rt('/submit-book', methods=["POST"])
    def submit_book(book_name: str, book_author: str, book_genre: str):
        """Handle book submission POST requests.
        
        Args:
            book_name (str): The title of the book
            book_author (str): The author of the book
            book_genre (str): The genre of the book
            
        Returns:
            str: Updated book list HTML
        """
        add_book(book_name, book_author, book_genre)
        return render_book_list(get_books)