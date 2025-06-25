
from typing import Any
from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    RadioField,
)

from wtforms.fields.core import UnboundField
from wtforms.form import BaseForm
from wtforms.validators import (
    DataRequired,
    InputRequired,
    StopValidation

)

from wtforms.csrf.core import CSRF
from flask_jwt_extended import get_jwt
from app.forms.common_widgest import MultiCheckboxField

class JWTCSRF(CSRF):
    def setup_form(self, form: BaseForm) :
        self.csrf_context = form.meta.csrf_context
        return super(JWTCSRF,self).setup_form(form)
    
    def generate_csrf_token(self, csrf_token): 
        token = get_jwt()
        csrf = token['csrf']
        return csrf

    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF')
class MultiCheckboxAtLeastOne():
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
