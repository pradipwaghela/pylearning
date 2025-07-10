from app.user.models import UserDAO

class UserController():
    def __init__(self):
        pass 

    def get_user(self,username):
        return UserDAO.get_user_by_username(username=username)