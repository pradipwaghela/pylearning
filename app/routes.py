from flask import render_template , flash , redirect
import random
import json

from PyMovieDb import IMDB

from app import app
from app.forms import MovieForm
from app.scrapIMDB import ScrapeIMDBTitle

def getMovieids(language,geners):
     IMDBObj = ScrapeIMDBTitle()
     ids = IMDBObj.getIMDBTitles(lan=language,geners=geners)
     return ids
def getRandomMovie(id):
     imdb = IMDB()
     res = imdb.get_by_id(id)
     data = json.loads(res)
     movie_name = data['name']
     movie_lan = data['review']['inLanguage']
     movie_genre = data['genre']
     movie_creator = data['director'][0]['name']
     movie_url = data['url']
     movie_imdb_rating = data['rating']['ratingValue']
     return movie_name , movie_lan , movie_genre , movie_creator , movie_url ,movie_imdb_rating

def notify_():
  print("I'm requesting This")  
@app.before_request()

@app.route('/',methods=["Post","Get"])
@app.route('/index',methods=["Post","Get"])
def index():
   form=MovieForm()
   if form.validate_on_submit():
     language = form.languages.data
     geners = form.movie_geners.data
     random_movie_id = random.choice(getMovieids(language,geners))
     movie_name , movie_lan , movie_genre , movie_creator , movie_url ,movie_imdb_rating = getRandomMovie(random_movie_id)
     movie_details = f"Movie Deatils :- \n\n Movie Name :- {movie_name} \n Movie Geners :- {movie_genre} \n Movie Language :- {movie_lan} \n Movie Director :- { movie_creator } \n Movie IMDB rating :- {movie_imdb_rating} \n Movie URL :- {movie_url}"
     msg = movie_details.split('\n')
     flash(msg)
     return redirect('/index')
   return render_template('index.html',form=form)