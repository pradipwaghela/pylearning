from app.utils import BaseDAO

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__("users")

    def get_user_by_username(self,username):
        query = {
            "username" : username
        }
        return BaseDAO.find_one(self,query=query,projection=None)