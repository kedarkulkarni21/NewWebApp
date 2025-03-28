"""
Book-related view components
"""

from fasthtml.common import Article, Button, Div, Em, Fieldset, Footer, Form, Header, Hr, Input, P, Small

from views.components import footer, info_text

def render_book(entry):
    """Create HTML representation of a single book.
    
    Args:
        entry (dict): Book data dictionary
        
    Returns:
        tuple: HTML components representing a book
    """
    return (
        Article(
            Header(f"Name: {entry['book_name']}"),
            P(f"Author: {entry['book_author']}"),
            Footer(Small(Em(f"Genre: {entry['book_genre']}"))),
        ),
    )

def render_book_list(get_books_func):
    """Render the complete list of books.
    
    Args:
        get_books_func: Function to retrieve books from the database
    
    Returns:
        Div: HTML component containing all books
    """
    books = get_books_func()
    return Div(
        *[render_book(book) for book in books],
        id="book-list",
    )

def render_book_form():
    """Render the book submission form.
    
    Returns:
        Form: HTML form component for book submission
    """
    return Form(
        Fieldset(
            Input(
                type="text",
                name="book_name",
                placeholder="Book Name",
                required=True,
                maxlength=50
            ),
            Input(
                type="text",
                name="book_author",
                placeholder="Book Author",
                required=True,
                maxlength=50
            ),
            Input(
                type="text",
                name="book_genre",
                placeholder="Book Genre",
                required=True,
                maxlength=50
            ),
            Button("Submit", type="submit"),
        ),
        method="POST",
        hx_post="/submit-book",
        hx_target="#book-list",
        hx_swap="outerHTML",
        hx_on__after_request="this.reset()",
    )

def render_main_content(get_books_func):
    """Render the main page content.
    
    Args:
        get_books_func: Function to retrieve books from the database
    
    Returns:
        Div: HTML component with the main page content
    """
    return Div(
        info_text("Suggest me a book!"),
        render_book_form(),
        footer(),
        Hr(),
        render_book_list(get_books_func),
    )