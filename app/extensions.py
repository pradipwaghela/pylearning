from  flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_migrate import Migrate


db = PyMongo()
login = LoginManager()
migrate = Migrate()

