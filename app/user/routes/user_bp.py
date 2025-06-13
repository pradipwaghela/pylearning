"""movie_bp.py
Contains routes of the application
user -> Main blue print

"""
from flask import Blueprint 

from app.user.controllers import UserController

user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
def login():
    """Login Route"""
    return UserController.login()


@user.route("/register", methods=["GET", "POST"])
def register():
    """Signup user route"""
    return UserController.register()

@user.route("/logout")
def logout():
    """Logout user route"""
    return UserController.logout()