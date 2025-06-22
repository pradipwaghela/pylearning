from flask_jwt_extended import create_access_token , create_refresh_token , get_csrf_token ,get_jwt_identity


class Auth():
    def __init__(self) -> None:
        pass
    def genrate_token(self,user_details):
        access_token = create_access_token(identity=user_details)
        return access_token ,  create_refresh_token(identity=user_details) , get_csrf_token(access_token)
    def validate_token(self,token):
        pass 
    def refresh_token(self,refresh_token,user_details):
        pass 
    def get_user_identity(self):
        return get_jwt_identity()