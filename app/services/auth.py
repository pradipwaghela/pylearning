from datetime import datetime, timezone, timedelta

from flask_jwt_extended import create_access_token , create_refresh_token , get_csrf_token, get_jwt_identity , verify_jwt_in_request, get_jwt




class Auth():
    def __init__(self) -> None:
        pass
    def genrate_token(self,user_details,claims):
        access_token = create_access_token(identity=user_details,additional_claims=claims)
        get_csrf_token(access_token)
        return access_token ,  create_refresh_token(identity=user_details,additional_claims=claims) 
    def validate_token(self,token):
        pass 
    def refresh_token(self,refresh_token,user_details):
        pass 
    def get_user_identity(self):
        return get_jwt_identity()
    def verify_request(self):
        return verify_jwt_in_request(optional=True)
    
    def create_csrf_token(self):
        return get_csrf_token()
    
    @staticmethod
    def refresh_expiring_jwts():
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            return create_access_token(identity=get_jwt_identity())
        return  None
    
