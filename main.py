import os

from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

app,rt = fast_app(
    hdrs = (Link(rel="icon", type="assets/x-icon", href="/assets/favicon.png"),),
)

def add_book(book_name, book_author, book_genre):
    supabase.table("MyLibrary").insert(
        {
            "book_name": book_name,
            "book_author": book_author,
            "book_genre": book_genre,
        }
    ).execute()

def get_books():
    response = (
        supabase.table("MyLibrary").select("*").order("id", desc=True).execute()
    )
    return response.data

def render_book(entry):
    return (
        Article(
            Header(f"Name: {entry['book_name']}"),
            P(f"Author: {entry['book_author']}"),
            Footer(Small(Em(f"Genre: {entry['book_genre']}"))),
        ),
    )

def render_book_list():
    books = get_books()

    return Div(
        *[render_book(entry) for entry in books],
        id="book-list",
    )


def render_signup():
    signup_form = Form(
        Fieldset(
            Input(
                type="text",
                name="username",
                placeholder="Username",
                required=True,
                maxlength=25
            ),
            Input(
                type="password",
                name="password",
                placeholder="Password",
                required=True,
                maxlength=15
            ),
            Button("Sign Up", type="submit"),
        )
    )

    return Div(
        P(Em("Enter your username and password")),
        signup_form,
    )

def render_content():
    form = Form(
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

    return Div(
        P(Em("Suggest me a book!")),
        form,
        Div(
            "Made with ❤️ by Kedar Kulkarni",
        ),
        Hr(),
        render_book_list(),
    )

@rt('/signup')
def signup():
    return Titled("Sign Up", render_signup())

@rt('/')
def get(): 
    return Titled("My Library📚", render_content())

@rt('/submit-book', methods=["POST"])
def post(book_name : str, book_author : str, book_genre : str):
    add_book(book_name, book_author, book_genre)
    return render_book_list()

serve()