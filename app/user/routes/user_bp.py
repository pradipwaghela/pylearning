from flask import Blueprint

from app.user.controllers import UserController 
user_bp = Blueprint("user",__name__)


@user_bp.route("/<username>",methods=["GET"])
def get_user_details(username):
    return  UserController.get_user(username=username)

@user_bp.route("/update/<username>",methods=["GET","POST"])
def update_user_details(username):
    pass

@user_bp.route("/register",methods=["POST"])
def register_user():
    pass
