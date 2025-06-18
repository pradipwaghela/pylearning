
from flask_login import current_user,logout_user 
from flask import render_template, flash, redirect, url_for, session

from app.user.forms import LoginForm ,RegistrationForm
from app.user.models import User


class UserController():
    
    def login(self):
        """Login Route"""
        if session.get('username') is True:
            return redirect(url_for("movie_suggest.index"))
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            data,status_code = User.login(username,password)
            if status_code == 200 :
                session["username"] = username
                return redirect(url_for("movie_suggest.index"))
            else : 
                flash(data["error"])
        return render_template("login.html", title="Sign In", form=form)
    
    def register(self):
        """Signup user route"""
        if session.get('username') is True:
            return redirect(url_for("movie_suggest.index"))
        form = RegistrationForm()
        if form.validate_on_submit():
            username = form.username.data
            email=form.email.data
            password = form.password.data
            data , status_code = User.register(username,password,email)
            if status_code == 200 :
                flash(data["message"])
                return redirect(url_for("user.login"))
            else : 
                flash(data["error"])
        return render_template("register.html", title="Register", form=form)
    
    def logout(self):
        """Logout user route"""
        session.pop('username' ,default= None)
        return redirect(url_for("movie_suggest.index"))
    
