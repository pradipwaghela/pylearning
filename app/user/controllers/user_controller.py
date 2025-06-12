
from flask_login import current_user, login_user, logout_user 
from flask import render_template, flash, redirect, url_for
import sqlalchemy as sa

from app.user.forms import LoginForm ,RegistrationForm
from app.extensions import db
from app.user.models import User


class UserController():
    
    def login(self):
        """Login Route"""
        if current_user.is_authenticated:
            return redirect(url_for("movie_suggest.index"))
        form = LoginForm()
        if form.validate_on_submit():
            user = db.session.scalar(
                sa.select(User).where(User.username == form.username.data)
            )
            if user is None or not user.check_password(form.password.data):
                flash("Invalid username or password")
                return redirect(url_for("movie_suggest.login"))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("movie_suggest.index"))
        return render_template("login.html", title="Sign In", form=form)
    
    def register(self):
        """Signup user route"""
        if current_user.is_authenticated:
            return redirect(url_for("movie_suggest.index"))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Congratulations, you are now a registered user!")
            return redirect(url_for("movie_suggest.login"))
        return render_template("register.html", title="Register", form=form)
    
    def logout(self):
        """Logout user route"""
        logout_user()
        return redirect(url_for("movie_suggest.index"))
    
