
import logging
from flask import Blueprint, redirect, url_for

from flask_jwt_extended import set_access_cookies

from app.services import Auth

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