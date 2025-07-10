from flask import Blueprint

user_bp = Blueprint("user",__name__)

@user_bp.route("<username>")
def user_update():
    pass 
