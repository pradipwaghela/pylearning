
import logging

from app.constants import User_Endpoints
from app.services  import JWTAuth
from app.extensions import csrf
from flask import  redirect, url_for, request
from flask_jwt_extended import set_access_cookies

def before_request():
    """
    Pre request steps 
    """
    request_endpoint = request.path
    protected_endpoints = User_Endpoints["protected"]
    if request_endpoint in protected_endpoints :
        JWTAuth.validate_token()
    logging.info("User trying to access [%s] ", request_endpoint)



     
