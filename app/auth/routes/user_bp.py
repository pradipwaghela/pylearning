"""movie_bp.py
Contains routes of the application
user -> Main blue print

"""
from flask import Blueprint 

from app.auth.controllers import AuthController

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET", "POST"])
@auth.route("/login", methods=["GET", "POST"])
def login():
    """Login Route"""
    return AuthController.login()


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Signup user route"""

    return AuthController.register()

@auth.route("/logout")
def logout():
    """Logout user route"""
    return AuthController.logout()