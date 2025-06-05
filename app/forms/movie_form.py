
from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    RadioField,
)

from wtforms.validators import (
    DataRequired,
    InputRequired,

)

from app.forms.common_widgest import MultiCheckboxField


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
