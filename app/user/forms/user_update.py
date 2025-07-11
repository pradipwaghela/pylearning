
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

class UpdateUser(FlaskForm):
    username = StringField("Username",render_kw={'disabled': True})
    email = StringField("Email",render_kw={'disabled': True})
    firstname = StringField("Firstname", validators=[DataRequired()])
    lastname = StringField("Lastname", validators=[DataRequired()])
    save =  SubmitField("Save")

