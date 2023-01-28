import os

from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config):
    app: Flask = Flask(__name__)
    app.config.from_object(config)
    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from PythonAPI.API.accounts.routes import accounts
    from PythonAPI.API.customers.routes import users
    from PythonAPI.API.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(accounts)
    app.register_blueprint(main)

    return app
