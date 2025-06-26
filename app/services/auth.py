"""
JWT user authentication service file 
"""


import time

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_csrf_token,
    get_jwt_identity,
    get_jwt,
)


class Auth:
    '''
    JWT Uer Authentication class 
    '''
    def __init__(self) -> None:
        pass

    def genrate_token(self, user_details, claims):
        """ 
        Genrate JWT access token and refers token against identity and claims

        Args:
            user_details (): User identity i.e username/email.
            claims (_dict_): Additional claims like first name last name, etc. 

        Returns:
            _tuple_: access_token , refresh_token 
        """
        access_token = create_access_token(
            identity=user_details, additional_claims=claims
        )
        get_csrf_token(access_token)
        return access_token, create_refresh_token(
            identity=user_details, additional_claims=claims)

    def validate_token(self, token):
        """Valide JWT token 

        Args:
            token (_str_): JWT access token 
        """
        pass


    def get_user_identity(self):
        """
        Get the current identity of the login user

        Returns:
            JWT identity 
        """
        return get_jwt_identity()

    @staticmethod
    def refresh_expiring_jwts():
        """Refresh JWT token 
        token will get refresh 5 min before expire

        Returns:
            access_token or None
        """
        exp_timestamp = get_jwt()["exp"]
        now = time.time()
        diff = exp_timestamp - now
        if diff <= 300:
            return create_access_token(identity=get_jwt_identity())
        return None
