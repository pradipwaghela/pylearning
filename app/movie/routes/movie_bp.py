"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from flask import Blueprint
from app.middlewares import unauthorized_callback, refresh_token 
from flask_jwt_extended import jwt_required

from app.extensions import (jwt , csrf)

from app.movie.controllers import MovieController
from app.services import Auth

movie_suggest = Blueprint("movie_suggest", __name__)

@jwt.unauthorized_loader(unauthorized_callback())


@movie_suggest.after_request
@jwt_required(refresh_token())



@movie_suggest.route("/home", methods=["Post", "Get"])
@csrf.exempt
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()
