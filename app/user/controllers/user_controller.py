"""
User authentication controller 
"""

from flask import render_template, flash, redirect, url_for, make_response
from flask_jwt_extended import set_access_cookies , set_refresh_cookies, unset_jwt_cookies 

from app.user.forms import LoginForm ,RegistrationForm
from app.user.models import User
from app.services import Auth

class UserController(): 
    
    def login(self):
        """Login Route"""
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            is_login , msg = User.login(username,password)
            if is_login :
                user_details = User.get_user_details(username)
                email = {
                    'email':user_details['email']
                }
                access_token , refresh_token = Auth.genrate_token(username,claims=email)
                
                
                response = make_response(redirect(url_for("movie_suggest.index")))
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response
            flash(msg)
        return render_template("login.html", title="Sign In", form=form)
    
    def register(self):
        """Signup user route"""
        form = RegistrationForm()
        if form.validate_on_submit():
            username = form.username.data
            email=form.email.data
            password = form.password.data
            is_registred , msg =  User.register(username,password,email)
            if is_registred:
                flash(msg)
                return redirect(url_for("user.login"))
            flash(msg)
        return render_template("register.html", title="Register", form=form)
    
    def logout(self):
        """Logout user route"""
        response = make_response(redirect(url_for("movie_suggest.index")) )
        unset_jwt_cookies(response)
        return response
        
    
