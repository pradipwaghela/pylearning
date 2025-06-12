"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from datetime import datetime, timezone
from flask import Blueprint 
from flask_login import  login_required ,current_user

from app.movie.controllers import MovieController
from app.extensions import db

movie_suggest = Blueprint("movie_suggest", __name__, template_folder="templates")



@movie_suggest.before_request
def before_request():
    if current_user is not None and current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()
        
@movie_suggest.route('/index', methods=["Post", "Get"])
@movie_suggest.route('/', methods=["Post", "Get"])
@login_required
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()

