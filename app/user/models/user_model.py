from werkzeug.security import generate_password_hash, check_password_hash

from app.utils import BaseDAO

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__("users")

    def get_user_by_username(self,username):
        query = {
            "username" : username
        }
        projection = {
            "_id" :  0,
            "password" :0
        }
        return BaseDAO.find_one(self,query=query,projection=projection)
    
    def get_user_by_email(self,email):
        query = {
            "email" : email
        }
        return BaseDAO.find_one(self,query=query,projection=None)
    
    def update_user_details(self,username,data):
        query = {
            "username" : username
        }  
        update_data = {
            '$set' : data
        }
        return BaseDAO.update_one(self,query=query,data=update_data,upsert=True)
    
    def set_password(self, password):
        """Genrate hash pasword 
        """
        return generate_password_hash(password)
    
    def register(self,username,password,email):
        """Register new user"""
        user = {
            'username' : username,
            'email' : email,
            'password' : self.set_password(password)
            }
        
        if BaseDAO.insert_one(self,user) :
            return True , f'Congratulation {username} , Your account is created.'
    def get_user_credentials(self,username):
        query = {
            "username" : username
        }
        projection = {
            "username" : 1,
            "password" : 1
        }
        return BaseDAO.find_one(self,query=query,projection=projection)
    def check_user_username(self,username):
        """
        Check if user exist using username 
        """
        return BaseDAO.find_one(self,query={'username' : username})
    
    def check_user_email(self,email):
        """
        Check is user exist using email
        """
        return  BaseDAO.find_one(self,query={'email' : email})