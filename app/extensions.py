from  flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf import CSRFProtect

mongo = PyMongo()
login = LoginManager()
migrate = Migrate()
jwt = JWTManager()
csrf = CSRFProtect()
