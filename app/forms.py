"""
forms.py
Contains form that required for application
MultiCheckboxField() -> Radio button form
MovieForm() -> Movie suggestion input form
"""

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectMultipleField, widgets, RadioField
from wtforms.validators import DataRequired, InputRequired


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
