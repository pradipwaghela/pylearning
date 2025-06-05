
from flask import render_template, flash, redirect, url_for

from app.forms import MovieForm
from app.services import get_movieids , get_random_movie

class MovieController():
    """sumary_line"""
    
    def __init__(self) -> None:
        pass
    def get_movie(self):
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
