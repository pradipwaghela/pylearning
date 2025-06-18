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
        self.db = mongo.db
        print(f"Mongodb {mongo.db}")
    
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password_hash , password):
        return check_password_hash(password_hash, password)
    
    def register(self,username,password,email):
        
        if not self.check_user_email(email) and not self.check_user_username(username):
            user = {
                '_id' : uuid.uuid4().hex,
                'username' : username,
                'email' : email,
                'password' : self.set_password(password)
                }
            
            if self.db.users.insert_one(user) :
                return jsonify({'message' : 'user created'}) , 200
        else :
            return jsonify ({"error" : 'Username/email already exists'}),400

    def login(self,username,password):
        user_details = self.get_user_details(username)
        if user_details:
            if self.check_password(password_hash=user_details["password"],password = password):
                return jsonify({"message" : "User logined"}),200
            else :
                return jsonify ({"error" : "Invalid password"}),401
        else : 
            return jsonify ({"error" : "Username  does not exists "}),401
            
    def get_user_details(self,username):
        if self.check_user_username(username):
            return self.db.users.find_one({'username' : username}) 
        return None
    def check_user_username(self,username):
       if  self.db.users.find_one({'username' : username}):
           return True
       return False
    
    def check_user_email(self,email):
       if  self.db.users.find_one({'username' : email}):
           return True
       return False
    
    
# @login.user_loader
# def load_user(id):
#     """
#     User loader function to get the user from the database
#     """
#     return db.session.get(User, int(id))