"""
User authentication controller 
"""

from flask import render_template, flash, redirect, url_for, make_response
from flask_jwt_extended import set_access_cookies , set_refresh_cookies, unset_jwt_cookies 

from app.auth.forms import LoginForm 
from app.auth.models import Auth
from app.user.models import UserDAO

from app.services import JWTAuth

class AuthController(): 
    
    def login(self):
        """Login Route"""
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            is_login , msg = Auth.login(username,password)
            if is_login :
                user_details = UserDAO.get_user_by_username(username)
                email = {
                    'email':user_details['email']
                }
                access_token , refresh_token = JWTAuth.genrate_token(username,claims=email)
                
                
                response = make_response(redirect(url_for("movie_suggest.index")))
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response
            flash(msg)
        return render_template("user/login.html", title="Sign In", form=form)
    
    
    def logout(self):
        """Logout user route"""
        response = make_response(redirect(url_for("auth.login")) )
        unset_jwt_cookies(response)
        return response
        
    
