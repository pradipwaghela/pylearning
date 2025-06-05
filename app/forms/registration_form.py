import sqlalchemy as sa

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

from app.models import User
from app import db

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

        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        """
        Validate User Email
        Args :
            email

        """

        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("Please use a different email address.")
