from app.utils.base_model import BaseDAO 
from app.user.models import UserDAO
class MovieDAO(BaseDAO):
    def __init__(self):
        super().__init__(collection="movies")
    
    def add_movie_wishlist(self,username):
        UserDAO.get_user_id(username=username)
        

