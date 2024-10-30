# Flask application initialization

from flask import Flask
from models import create_user_table

def ProjApp():
    app = Flask(__name__)
    app.secret_key = 'MyOwnSeceretKey7'
    
    create_user_table()
    
    #Registration of Blueprints
    from .routes import main_route
    app.register_blueprint(main_route)
    
    return app
    
    

