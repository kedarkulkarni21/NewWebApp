"""
Authentication-related route handlers
"""

from fasthtml.common import Titled
from views.auth_views import render_signup_form

def register_auth_routes(rt):
    """Register all authentication-related routes.
    
    Args:
        rt: Route handler from the FastHTML app
    """
    
    @rt('/signup')
    def signup():
        """Handle signup page requests.
        
        Returns:
            str: HTML for signup page
        """
        return Titled("Sign Up", render_signup_form())
    
    # Additional auth routes can be added here
    # @rt('/login')
    # def login():
    #     pass
    
    # @rt('/logout')
    # def logout():
    #     pass