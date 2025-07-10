"""
app init file
create_app() -> Return  flask app

"""

import os

from dotenv import load_dotenv

from flask import Flask

from app.services.mv_logging import setup_logger

from config import ProductionConfig, DevelopmentConfig, TestingConfig
from app.extensions import mongo, jwt, csrf, setup_folder 
from app.middlewares import  before_request

from app.services import JWTAuth

def create_app():
    """
    Create flask app in Application factory Pattern
    Return: Flask app
    """
    
    app = Flask(__name__)
    with app.app_context():
        
        load_dotenv()  # loading envrionement variables
        

        env_type = os.environ.get("FLASK_ENV", default="Development")

        if env_type == "Development":
            app.config.from_object(DevelopmentConfig)

        elif env_type == "Production":
            app.config.from_object(ProductionConfig)

        elif env_type == "Testing":
            app.config.from_object(TestingConfig)
        
        mongo.init_app(app)
        jwt.init_app(app)
        csrf.init_app(app)
        
        setup_folder() # Setup required folder strucutre
        setup_logger() # Setup logger
        
        #Process requests
        app.before_request(before_request)
        
        # Import and register blueprints
        from app.movie.routes import movie_suggest
        from app.auth.routes import auth
        from app.user.routes import user_bp
        app.register_blueprint(movie_suggest)
        app.register_blueprint(auth)
        app.register_blueprint(user_bp,url_prefix="/user")
        # app.context_processor(JWTAuth.inject_csrf_token)

    return app
