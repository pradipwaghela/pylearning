"""routes.py
Contains routes of the application
movie_suggest -> Main blue print

"""

import sqlalchemy as sa
from datetime import datetime, timezone

from flask import render_template, flash, redirect, Blueprint, url_for
from flask_login import current_user, login_user, logout_user , login_required

from app.extensions import db

from app.models import User
from app.forms import MovieForm, LoginForm, RegistrationForm
from app.services.services import get_movieids, get_random_movie

movie_suggest = Blueprint("movie_suggest", __name__, template_folder="templates")


@movie_suggest.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

@movie_suggest.route('/index', methods=["Post", "Get"])
@movie_suggest.route('/', methods=["Post", "Get"])
@login_required
def index():
    """Landing/Welcome Page route

    Returns:
        render_template: Render home page
    """
    form = MovieForm()
    if form.validate_on_submit():
        language = form.languages.data
        geners = form.movie_geners.data
        movie_ids = get_movieids(language, geners)
        (
            movie_name,
            movie_lan,
            movie_genre,
            movie_creator,
            movie_url,
            movie_imdb_rating,
        ) = get_random_movie(movie_ids)
        movie_details = f"""Movie Deatils :- \n\n Movie Name :- {movie_name}
                            \n Movie Geners :- {movie_genre} 
                            \n Movie Language :- {movie_lan} 
                            \n Movie Director :- { movie_creator } 
                            \n Movie IMDB rating :- {movie_imdb_rating} 
                            \n Movie URL :- {movie_url}"""
        msg = movie_details.split("\n")
        flash(msg)
        return redirect(url_for('movie_suggest.index'))
    return render_template("index.html", form=form)


@movie_suggest.route("/login", methods=["GET", "POST"])
def login():
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


@movie_suggest.route("/register", methods=["GET", "POST"])
def register():
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


@movie_suggest.route("/logout")
def logout():
    """Logout user route"""

    logout_user()
    return redirect(url_for("movie_suggest.index"))
