import os

from flask import Flask


def create_app(config):
    app: Flask = Flask(__name__)
    app.config.from_object(config)
    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key

    from PythonAPI.FlaskAPI.AccountRoutes.CreateAccountBlueprint import Account

    app.register_blueprint(Account)
