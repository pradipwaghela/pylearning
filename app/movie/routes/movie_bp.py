"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from datetime import datetime, timezone
from flask import Blueprint, session, url_for

from app.movie.controllers import MovieController

movie_suggest = Blueprint("movie_suggest", __name__)



@movie_suggest.before_request
def before_request():
    if session.get("username") is  False:
        url_for('/login')
        
@movie_suggest.route('/index', methods=["Post", "Get"])
@movie_suggest.route('/', methods=["Post", "Get"])
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()

