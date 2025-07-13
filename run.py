import os 

from flask import redirect, url_for
from app import create_app , mongo

from app.auth.models import  Auth 

app = create_app()

@app.shell_context_processor
def shell():
    """
    Set flask shell context 

    Returns:
        db : _description_
    """
    return {
        "db": mongo.db,
        "aut" : Auth
    }


@app.route("/",methods=["GET"])
def landing_page():
    return redirect(url_for("auth.login"))  
      
if __name__ == '__main__' :
    port  = os.environ.get("FLASK_RUN_PORT",default=5000)
    ip = os.environ.get("FLASK_RUN_HOST",default="0.0.0.0")
    app.run(host=ip,port=port,debug=True)
