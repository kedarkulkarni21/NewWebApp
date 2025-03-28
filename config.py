"""
Application configuration settings
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
APP_NAME = "My Library📚"

# Database settings
DB_TABLE_BOOKS = "MyLibrary"