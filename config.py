"""Config.py 
    File contains class for flask environment setup 
    Config() -> Default configd 
    ProductionConfig() -> Producation configs
    DevelopmentConfig() -> Development configs
    TestingConfig() -> Testing configs 
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Class with default configutaion
       Orveride variable of the class
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "f7628218af8b4fb16c375cf31e01c9afa13cdba996d8b7dc5b11d43a6423c5a8"
    WTF_CSRF_SECRET_KEY = "f7628218af8b4fb16c375cf31e01c9afa13cdba996d8b7dc5b11d43a6423c5a8"
    MONGO_URI = os.environ.get('MONGO_URI') or "mongodb://localhost:27017/movie_db"


class ProductionConfig(Config):
    """Class contains producation configuration"""
    ENV_TYPE = "Production"


class DevelopmentConfig(Config):
    """Class contains Development configurations"""
    ENV_TYPE = "Development"
    

class TestingConfig(Config):
    """Class contains testing configurations """    
    ENV_TYPE = "Testing"
