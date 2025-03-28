"""
Book model and database operations
"""

from db.database import get_db_client
from config import DB_TABLE_BOOKS

# Get database client
db = get_db_client()

class Book:
    """Book model representing a book in the library."""
    
    def __init__(self, name, author, genre, id=None):
        """Initialize a new Book instance.
        
        Args:
            name (str): The title of the book
            author (str): The author of the book
            genre (str): The genre of the book
            id (int, optional): The book ID. Defaults to None.
        """
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
    
    def save(self):
        """Save the book to the database.
        
        Returns:
            Book: The saved book instance with ID updated
        """
        data = {
            "book_name": self.name,
            "book_author": self.author,
            "book_genre": self.genre,
        }
        
        response = db.table(DB_TABLE_BOOKS).insert(data).execute()
        self.id = response.data[0].get("id")
        return self
    
    @classmethod
    def get_all(cls):
        """Retrieve all books from the database.
        
        Returns:
            list: List of Book instances
        """
        response = db.table(DB_TABLE_BOOKS).select("*").order("id", desc=True).execute()
        
        books = []
        for book_data in response.data:
            book = cls(
                name=book_data.get("book_name"),
                author=book_data.get("book_author"),
                genre=book_data.get("book_genre"),
                id=book_data.get("id")
            )
            books.append(book)
            
        return books