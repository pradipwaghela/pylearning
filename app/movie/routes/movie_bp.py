"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from flask import Blueprint

from app.movie.controllers import MovieController
from flask_jwt_extended import jwt_required

movie_suggest = Blueprint("movie_suggest", __name__)


@movie_suggest.route('/home', methods=["Post", "Get"])
@jwt_required()
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()
