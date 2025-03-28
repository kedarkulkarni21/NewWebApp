"""
Database connection and client setup
"""

from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

def get_db_client():
    """Initialize and return Supabase client for database operations.
    
    Returns:
        Client: Initialized Supabase client
    
    Raises:
        ValueError: If required environment variables are missing
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Missing required environment variables for database connection")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Make sure the function is available for import
__all__ = ['get_db_client']