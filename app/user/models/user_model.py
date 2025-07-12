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