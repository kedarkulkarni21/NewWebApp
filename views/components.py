"""
Reusable UI components
"""

from fasthtml.common import Div, Em, P

def footer():
    """Render the application footer.
    
    Returns:
        Div: Footer component
    """
    return Div(
        "Made with ❤️ by Kedar Kulkarni",
    )

def info_text(text):
    """Render emphasized informational text.
    
    Args:
        text (str): Text content
        
    Returns:
        P: Paragraph with emphasized text
    """
    return P(Em(text))