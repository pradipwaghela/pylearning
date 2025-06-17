import uuid

from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from bson import objectid

from app.extensions import db , login

class User():
    """User Model

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self) -> None:
        pass

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self._id
    
    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def register(self,username,password,email):
        
        if not self.check_user_email(email) and not self.check_user_username(username):
            user = {
                '_id' : uuid.uuid4().hex,
                'username' : username,
                'email' : email,
                'password' : self.set_password(password)
                }
            
            if db.users.insert_one(user) :
                return jsonify({'message' : 'user created'}) , 200
        else :
            return jsonify ({"error" : 'Username/email already exists'}),400

    def check_user_username(self,username):
       
       if  db.users.find_one({'username' : username}):
           return True
       return False
    
    def check_user_email(self,email):
       if  db.users.find_one({'username' : email}):
           return True
       return False
    
    def __repr__(self):
        return f'<User {self.username}>'
    
@login.user_loader
def load_user(id):
    """
    User loader function to get the user from the database
    """
    return db.session.get(User, int(id))