from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField , SelectMultipleField , widgets , RadioField
from wtforms.validators import DataRequired , InputRequired 

class MultiCheckboxField(SelectMultipleField):
  widget = widgets.ListWidget(prefix_label=False)
  option_widget = widgets.CheckboxInput()

class MovieForm(FlaskForm):
  movie_geners_ = ("Horror","Action","Drama","Romantic")
  movie_geners = MultiCheckboxField("Movie Geners :- ",choices=movie_geners_, validators=[DataRequired()])
  languages = RadioField('Languages:-',
                       choices=['Hindi', 'Marathi', 'English'],
                       validators=[InputRequired()])
  submit=SubmitField('Suggest')