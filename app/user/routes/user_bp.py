from flask import Blueprint, render_template, url_for, request

from app.user.controllers import UserController 
user_bp = Blueprint("user",__name__)


@user_bp.route("/?<username>",methods=["GET"])
def get_user_details(username):
    return UserController.get_user(username=username)

@user_bp.route("/update/<username>",methods=["POST","GET"])
def update_user_details(username):
    return UserController.update_user(username=username)

@user_bp.route("/register",methods=["POST","GET"])
def register_user():
    return UserController.register()
