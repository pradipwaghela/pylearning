"""
Movie Module Service file
"""

import random
import json
import logging

from PyMovieDb import IMDB

from app.movie.services.scrape_imdb_titles import ScrapeIMDBTitle


def get_movieids(language, geners):
    """
    Get IMDB movie ids 

    Args:
        language (string): Language of the movies 
        geners (string ): Geners of the movies 

    Returns:
        list : IMDB movie unique Id 
    """
    try :    
        imdb_obj = ScrapeIMDBTitle()
        return imdb_obj.get_imdb_titles(lan=language, geners=geners)
    except Exception as e:
        logging.error("Error while getting movie ids %s",e)


def get_random_movie(ids):
    """Get movie details from ID 

    Args:
        ids (string): IMDB unique ID 

    Returns:
        tuple : return  movie name,language,geners,creator,IMDB url and IMDB rating  
    """
    try : 
        random_movie = random.choice(ids)
        imdb = IMDB()
        res = imdb.get_by_id(random_movie)
        data = json.loads(res)
        movie_name = data["name"]
        movie_lan = data["review"]["inLanguage"]
        movie_genre = data["genre"]
        movie_creator = data["director"][0]["name"]
        movie_url = data["url"]
        movie_imdb_rating = data["rating"]["ratingValue"]
        return (
            random_movie,
            movie_name,
            movie_lan,
            movie_genre,
            movie_creator,
            movie_url,
            movie_imdb_rating,
        )
    except Exception as e :
        logging.error("Error while getting movie details %s", e)
        return None
