import request
import logging

from app.constants import User_Endpoints
from app.services  import Auth
from flask import  redirect, url_for
from flask_jwt_extended import set_access_cookies

def before_request():
    """
    Pre request steps 
    """
    request_endpoint = request.path
    protected_endpoints = User_Endpoints["protected"]
    if request_endpoint in protected_endpoints :
        Auth.validate_token()
    logging.info("User trying to access [%s] ", request_endpoint)



def unauthorized_callback(callback):
    '''
    If not a valid JWT token then redirect user to login page 
    '''
    try :
        logging.debug("Not a valide JWT token please login back in ")
        return redirect(url_for('user.login'))
    except Exception as e :
        logging.error("Error while redirecting user for re-login %s",e)
        
def refresh_token(response):
    '''
    Refresh JWT token if expired or going to expire 
    '''
    try:
        access_token = Auth.refresh_expiring_jwts()
        if access_token:
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError) as e:
        logging.error("Error while refreshing token %s ",e)
        return response