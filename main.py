import os

from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

load_dotenv()

#Initialize Supabase Client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

app,rt = fast_app(
    hdrs = (Link(rel="icon", type="assets/x-icon", href="/assets/favicon.png"),),
)

def add_book(book_name, book_author, book_year):
    supabase.table("MyLibrary").insert(
        {
            "book_name": book_name,
            "book_author": book_author,
            "book_year": book_year,
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
            Footer(Small(Em(f"Year: {entry['book_year']}"))),
        ),
    )

def render_book_list():
    books = get_books()

    return Div(
        *[render_book(entry) for entry in books],
        id="book-list",
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
                name="book_year",
                placeholder="Book Year",
                required=True,
                maxlength=4
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
        P(Em("Suggest a book!")),
        form,
        Div(
            "Made with ❤️ by Kedar Kulkarni",
        ),
        Hr(),
        render_book_list(),
    )

@rt('/')
def get(): 
    return Titled("My Library📚", render_content())

@rt('/submit-book', methods=["POST"])
def post(book_name : str, book_author : str, book_year : int):
    add_book(book_name, book_author, book_year)
    return render_book_list()

serve()