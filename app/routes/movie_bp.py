"""routes.py
Contains routes of the application
movie_suggest -> Main blue print

"""
from datetime import datetime, timezone
from flask import Blueprint , g 
from flask_login import  login_required ,current_user

from app.controllers import MovieController, UserController
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


@movie_suggest.route("/login", methods=["GET", "POST"])
def login():
    """Login Route"""
    return UserController.login()


@movie_suggest.route("/register", methods=["GET", "POST"])
def register():
    """Signup user route"""
    return UserController.register()

@movie_suggest.route("/logout")
def logout():
    """Logout user route"""
    return UserController.logout()
