"""
app init file 
create_app() -> Return  flask app 

"""
import os

from dotenv import load_dotenv

from flask import Flask

from config import ProductionConfig, DevelopmentConfig, TestingConfig
from app.routes import movie_suggest


def create_app():
    """Create flask app
    Return: Flask app
    """
    load_dotenv() #loading envrionement variables
    app = Flask(__name__)


    env_type = os.environ.get("FLASK_ENV", default="Developmemt")

    if env_type == "Developmemt":
        app.config.from_object(DevelopmentConfig())
        
    elif env_type == "Production":
        app.config.from_object(ProductionConfig())
        
    elif env_type == "Testing":
        app.config.from_object(TestingConfig())
        
    #app.secret_key = "lol"
    print(f"Secret key is {app.config.get('SECRET_KEY')}")
    app.register_blueprint(movie_suggest)

    return app
