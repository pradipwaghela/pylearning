"""
forms.py
Contains form that required for application
MultiCheckboxField() -> Radio button form
MovieForm() -> Movie suggestion input form
"""

import sqlalchemy as sa

from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    SelectMultipleField,
    widgets,
    RadioField,
    StringField,
    PasswordField,
    BooleanField,
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    ValidationError,
    Email,
    EqualTo,
)

from app.models import User
from app import db


class MultiCheckboxField(SelectMultipleField):
    """
    Use to create checkbox

    Args:
        SelectMultipleField
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class MovieForm(FlaskForm):
    """
    Use to create movie suggestion form

    Args:
        FlaskForm
    """

    movie_geners_ = ("Horror", "Action", "Drama", "Romantic")
    movie_geners = MultiCheckboxField(
        "Movie Geners :- ", choices=movie_geners_, validators=[DataRequired()]
    )
    languages = RadioField(
        "Languages:-",
        choices=["Hindi", "Marathi", "English"],
        validators=[InputRequired()],
    )
    submit = SubmitField("Suggest")


class LoginForm(FlaskForm):
    """
    Use to create User Login page

    Args:
        FlaskForm
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


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
