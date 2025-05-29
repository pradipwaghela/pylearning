import os 

from app import create_app , db

from app.models import  User 

app = create_app()

@app.shell_context_processor
def shell():
    return {
        "db": db,
        "User" : User
    }
if __name__ == '__main__' :
    port  = os.environ.get("FLASK_RUN_PORT",default=5000)
    ip = os.environ.get("FLASK_RUN_HOST",default="0.0.0.0")
    app.run(host=ip,port=port,debug=True)
