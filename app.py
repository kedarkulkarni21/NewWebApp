"""
Library Management Application
Main application entry point with simplified imports
"""

import os
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import Link, fast_app, Titled, serve

# Load environment variables
load_dotenv()

# Setup database
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Create application
app, rt = fast_app(
    hdrs=(Link(rel="icon", type="assets/x-icon", href="/static/assets/favicon.png"),),
)

# Import route functions (moved after app initialization to avoid circular imports)
from routes.book_routes import register_book_routes
from routes.auth_routes import register_auth_routes

# Register routes
register_book_routes(rt, supabase)
register_auth_routes(rt)

if __name__ == "__main__":
    print("Starting Library Management Application...")
    serve()