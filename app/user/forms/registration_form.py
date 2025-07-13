
from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
)
from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    EqualTo,
)

from app.user.models import UserDAO

class RegistrationForm(FlaskForm):
    """
    Use to create User Signup  page

    Args:
        FlaskForm
    """

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        """
        Validate Username

        Args :
            username
        """
        user = UserDAO.check_user_username(username.data)
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        """
        Validate User Email
        Args :
            email

        """
        user = UserDAO.check_user_email(email.data)
        if user is not None:
            raise ValidationError("Please use a different email address.")
