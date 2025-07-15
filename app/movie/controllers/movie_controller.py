"""
Movie controller 
"""
import logging
from flask import render_template, flash,request

from app.movie.forms import MovieForm,WishlistMovieForm
from app.movie.services import get_movieids, get_random_movie
from app.services import JWTAuth

class MovieController:
    """
    Movie suggestion class 
    """

    def __init__(self) -> None:
        pass

    def get_movie(self):
        """Landing/Welcome Page route

        Returns:
            render_template: Render home page
        """
        try :
            identity = JWTAuth.get_user_identity()
            data = request
            form = MovieForm()
            if form.validate_on_submit():
                language = form.languages.data
                geners = form.movie_geners.data
                movie_ids = get_movieids(language, geners)
                (
                    movie_id,
                    movie_name,
                    movie_lan,
                    movie_genre,
                    movie_creator,
                    movie_url,
                    movie_imdb_rating,
                ) = get_random_movie(movie_ids)
                
                movie_details = {
                    "id" : movie_id,
                    "name": movie_name,
                    "geners": movie_genre,
                    "languages": movie_lan,
                    "director": movie_creator,
                    "rating": movie_imdb_rating,
                    "url": movie_url,
                }
                return render_template("movie/movie.html", movie=movie_details,username=identity)
        except TypeError :
            flash("No Movie found for selected input")
            logging.debug("No movie found for selected input")

        except Exception as e :
            flash("Error While suggesting movie Please Try Again")
            logging.error("Error while suggesting movie %s",e )

        return render_template("movie/index.html", form=form,username=identity)
    def show_movie(self):
        try:
            identity = JWTAuth.get_user_identity()
            form = WishlistMovieForm()
            if form.is_submitted():


                pass 
            elif request.method == "GET":
                form_data = request.form()

                pass 



        except Exception as e :
            pass
            
        
            
