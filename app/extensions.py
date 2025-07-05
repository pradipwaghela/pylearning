"""
Flask app extentions 
"""
import os 
import logging
from flask import current_app, request
from  flask_pymongo import PyMongo
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf import CSRFProtect

mongo = PyMongo()
migrate = Migrate()
jwt = JWTManager()
csrf = CSRFProtect()



def setup_folder():
    """
    Create folder structure of the application 
    """
    try:
        log_files_path = current_app.config.get("LOG_FILES_PATH")
        if not (os.path.exists(log_files_path)):
            logging.debug("Created log file path %s",log_files_path)
            os.makedirs(log_files_path,exist_ok=True)
    except Exception as e :
        logging.error("Error while creating folder structure %s",e)