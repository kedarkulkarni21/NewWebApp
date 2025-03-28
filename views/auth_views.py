"""
Authentication-related view components
"""

from fasthtml.common import Button, Div, Fieldset, Form, Input

from views.components import info_text

def render_signup_form():
    """Render the signup form.
    
    Returns:
        Div: HTML component with signup form
    """
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
        info_text("Enter your username and password"),
        signup_form,
    )