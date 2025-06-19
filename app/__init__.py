"""
app init file
create_app() -> Return  flask app

"""

import os

from dotenv import load_dotenv

from flask import Flask

import jinja2

from config import ProductionConfig, DevelopmentConfig, TestingConfig
from app.extensions import mongo


def create_app():
    """
    Create flask app in Application factory Pattern
    Return: Flask app
    """
    load_dotenv()  # loading envrionement variables
    
    app = Flask(__name__)
    
    env_type = os.environ.get("FLASK_ENV", default="Development")

    if env_type == "Development":
        app.config.from_object(DevelopmentConfig)

    elif env_type == "Production":
        app.config.from_object(ProductionConfig)

    elif env_type == "Testing":
        app.config.from_object(TestingConfig)
    
    mongo.init_app(app)
    #Load Template
    # Import and register blueprints
    from app.movie.routes import movie_suggest
    from app.user.routes import user

    app.register_blueprint(movie_suggest)
    
    app.register_blueprint(user)

    

    
    return app
