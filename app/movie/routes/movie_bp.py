"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from flask import Blueprint, session

from app.movie.controllers import MovieController
from flask_jwt_extended import (
    jwt_required,
    set_access_cookies,
    get_csrf_token,
    verify_jwt_in_request,
)
from app.extensions import jwt , csrf
from app.services import Auth

movie_suggest = Blueprint("movie_suggest", __name__)

# @jwt.unauthorized_loader
# def unauthorized_callback(callback):

#     print("Not a valide JWT")
#     return redirect(url_for('user.login'))

# @movie_suggest.after_request
# def refresh_token(response):
#     try:
#         access_token = Auth.refresh_expiring_jwts()
#         if access_token:
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original response
#         return response


@movie_suggest.route("/home", methods=["Post", "Get"])
@csrf.exempt
@jwt_required()
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()
