import os

from flask import Flask
from flask_cors import CORS

def create_app(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key

    from PythonAPI.FlaskAPI.AccountRoutes.CreateAccountBlueprint import create_account
    from PythonAPI.FlaskAPI.CustomerRoutes.LoginBlueprint import login

    app.register_blueprint(create_account)
    app.register_blueprint(login)
