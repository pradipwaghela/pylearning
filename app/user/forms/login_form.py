
from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
    BooleanField,
)

from wtforms.validators import (
    DataRequired,
)


class LoginForm(FlaskForm):
    """
    Use to create User Login page

    Args:
        FlaskForm
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")
