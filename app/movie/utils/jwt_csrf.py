from wtforms.csrf.core import CSRF
from flask_jwt_extended import get_jwt
from wtforms.form import BaseForm

class JWTCSRF(CSRF):
    """
    Custom JWT CSRF class 
    """
    
    def setup_form(self, form: BaseForm) :
        """
        override parent setup_form() method
        """
        self.csrf_context = form.meta.csrf_context
        return super(JWTCSRF,self).setup_form(form)
    
    def generate_csrf_token(self, csrf_token):
        """
        Get JWT http csrf string 
        """
        
        token = get_jwt()
        csrf = token['csrf']
        return csrf

    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF')
  