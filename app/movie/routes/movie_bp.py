"""movie_bp.py
Contains routes of the application
movie_suggest -> Main blue print

"""
import logging
from flask import Blueprint, redirect, url_for
from flask_jwt_extended import jwt_required, set_access_cookies

from app.extensions import (jwt , csrf)

from app.movie.controllers import MovieController
from app.services import JWTAuth

movie_suggest = Blueprint("movie_suggest", __name__)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    '''
    If not a valid JWT token then redirect user to login page 
    '''
    try :
        logging.debug("Not a valide JWT token please login back in ")
        return redirect(url_for('auth.login'))
    except Exception as e :
        logging.error("Error while redirecting user for re-login %s",e)
   


@movie_suggest.after_request
@jwt_required()
def refresh_token(response):
    '''
    Refresh JWT token if expired or going to expire 
    '''
    try:
        access_token = JWTAuth.refresh_expiring_jwts()
        if access_token:
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError) as e:
        logging.error("Error while refreshing token %s ",e)
        return response



@movie_suggest.route("/home", methods=["Post", "Get"])
@csrf.exempt
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    return MovieController.get_movie()
