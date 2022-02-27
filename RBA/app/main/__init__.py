from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # support for SQLalchemy to your flask applicatiom
from flask_bcrypt import Bcrypt  # hashing module

from .config import config_by_name 
# this is used for setting the enviorent like testing or devepoment etc


db = SQLAlchemy()  # creating the object of SQLAlchemy class
flask_bcrypt = Bcrypt()  #Instantiate bcrypt object in python.

def create_app(config_name):
    app = Flask(__name__)  # the app is created here
    app.config.from_object(config_by_name[config_name])  
    # The app.config_from_object () method loads configuration from a configuration object. This can be a configuration module, or any object with configuration attributes. Note that any configuration that was previously set will be reset when config_from_object () is called. If you want to set additional configuration you should do so after.
    db.init_app(app) 
    # need to see this function and have look
    #flask_bcrypt is working see it
    
    flask_bcrypt.init_app(app)

    return app