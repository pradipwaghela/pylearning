"""
User model file 
"""


from werkzeug.security import check_password_hash
from app.user.models import UserDAO

class Auth():
    """User Model

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self) -> None:
        pass
    


    def check_password(self, password_hash , password):
        """Check password provided by user """
        return check_password_hash(password_hash, password)
    
    def login(self,username,password):
        """
        Login user 
        """
        user_details = UserDAO.get_user_credentials(username)
        if user_details:
            if self.check_password(user_details["password"],password):
                return True , "User logined"
            else :
                return False ,  "Invalid password"
        else : 
            return False ,  "Username  does not exists"
            
    


    


    
