import uuid

from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from bson import objectid

from app.extensions import mongo

class User():
    """User Model

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self) -> None:
        pass
    
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password_hash , password):
        return check_password_hash(password_hash, password)
    
    def register(self,username,password,email):
        
            user = {
                '_id' : uuid.uuid4().hex,
                'username' : username,
                'email' : email,
                'password' : self.set_password(password)
                }
            if mongo.db.users.insert_one(user) :
                return True , f'Congratulation {username} , Your account is created.'

    def login(self,username,password):
        user_details = self.get_user_details(username)
        if user_details:
            if self.check_password(user_details["password"],password):
                return True , "User logined"
            else :
                return False ,  "Invalid password"
        else : 
            return False ,  "Username  does not exists"
            
    def get_user_details(self,username):
        if self.check_user_username(username):
            return mongo.db.users.find_one({'username' : username})
        return None
    
    def check_user_username(self,username):
      return mongo.db.users.find_one({'username' : username})

    
    def check_user_email(self,email):
       return mongo.db.users.find_one({'username' : email})

    
