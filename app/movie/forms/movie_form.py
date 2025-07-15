

from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    RadioField,
)

from wtforms.validators import (
    InputRequired,
    StopValidation

)


from app.forms.common_widgest import MultiCheckboxField
from app.movie.utils.jwt_csrf import JWTCSRF
      
class MultiCheckboxAtLeastOne():
    """
    Custom form validator for list 
    
    """
    def __init__(self, message=None):
        if not message:
            message = 'At least one option must be selected.'
        self.message = message

    def __call__(self, form, field):
        if len(field.data) == 0:
            raise StopValidation(self.message)
        
class MovieForm(FlaskForm):
    """
    Use to create movie suggestion form

    Args:
        FlaskForm
    """
    class Meta:
        """
        Setup Flask_WT CSRF for custom CSRF
        """
        
        csrf = True
        csrf_class = JWTCSRF 

    movie_geners_ = ("Horror", "Action", "Drama", "Romantic")
    movie_geners = MultiCheckboxField(
        "Movie Geners :- ", choices=movie_geners_, validators=[MultiCheckboxAtLeastOne()]
    )
    languages = RadioField(
        "Languages:-",
        choices=["Hindi", "Marathi", "English"],
        validators=[InputRequired()],
    )
    submit = SubmitField("Suggest")
