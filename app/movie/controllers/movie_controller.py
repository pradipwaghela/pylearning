"""
Movie controller 
"""
import logging
from flask import render_template, flash, request, redirect, url_for

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
            wishlistform = WishlistMovieForm()
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
                
                wishlistform.movie_id.data = movie_id
                wishlistform.name.data = movie_name
                wishlistform.geners.data = movie_genre
                wishlistform.languages.data = movie_lan
                wishlistform.director.data = movie_creator
                wishlistform.rating.data = movie_imdb_rating
                wishlistform.url.data = movie_url

                # movie_details = {
                #     "id" : movie_id,
                #     "name": movie_name,
                #     "geners": movie_genre,
                #     "languages": movie_lan,
                #     "director": movie_creator,
                #     "rating": movie_imdb_rating,
                #     "url": movie_url,
                # }
                return render_template("movie/movie.html", form=wishlistform,username=identity)
            if wishlistform.is_submitted():
                formdata = wishlistform.data
                movie_id = formdata.get("movie_id")
                movie_name = formdata.get("name")
                movie_lan =formdata.get("languages")
                movie_genre = formdata.get("geners")
                movie_creator = formdata.get("director")
                movie_url = formdata.get("url")
                movie_imdb_rating =formdata.get("rating")
                # return redirect(url_for('movie_suggest.show_movie',movie=movie_details))
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
            
        
            
