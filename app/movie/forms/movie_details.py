from flask_wtf import FlaskForm
from app.movie.utils.jwt_csrf import JWTCSRF
from wtforms import SubmitField,StringField

class WishlistMovieForm(FlaskForm):
    class meta:
        csrf = True
        csrf_class = JWTCSRF 
    
    movie_id = StringField('',render_kw= {'style': 'display: none'})
    name = StringField("Name",render_kw={'readonly':True})
    geners = StringField("Geners",render_kw={'readonly':True})
    languages = StringField("Languages",render_kw={'readonly':True})
    director = StringField("Director",render_kw={'readonly':True})
    rating = StringField("IMDB Rating")
    url = StringField("IMDB URL",render_kw={'readonly': True})
    add_wishlist = SubmitField("Add To Wishlist")
