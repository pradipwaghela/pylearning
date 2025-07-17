from app.utils.base_model import BaseDAO 
from app.user.models import UserDAO
class MovieDAO(BaseDAO):
    def __init__(self,username):
        super().__init__(collection="movies")
        self.user_id = UserDAO.get_user_id(username=username)

    def add_movie_wishlist(self,movie_data):
        movie_data["user_id"].append(self.user_id)
        return  BaseDAO.insert_one(self,data=movie_data)
    def check_wishlist_movie(self,imdb_id):

        query = {
            "imdb_id" : imdb_id,
            "user_id" : self.user_id
        }
        projection = {
            "movie_name" : 1
        } 
        return BaseDAO.find_one(self,query=query,projection=projection)





        
        

