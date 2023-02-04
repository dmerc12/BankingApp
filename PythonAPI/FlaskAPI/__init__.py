import os

from flask import Flask
from flask_cors import CORS

from PythonAPI.FlaskAPI.AccountRoutes.CreateAccountBlueprint import create_account
from PythonAPI.FlaskAPI.CustomerRoutes.LoginBlueprint import login
from PythonAPI.FlaskAPI.CustomerRoutes.CreateCustomerBlueprint import create_customer
from PythonAPI.FlaskAPI.CustomerRoutes.LogoutBlueprint import logout
from PythonAPI.FlaskAPI.CustomerRoutes.UpdateCustomerBlueprint import update_customer
from PythonAPI.FlaskAPI.CustomerRoutes.DeleteCustomerBlueprint import delete_customer
from PythonAPI.FlaskAPI.AccountRoutes.GetAllAccountsBlueprint import get_all_accounts

def create_app(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key

    app.register_blueprint(create_account)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(create_customer)
    app.register_blueprint(update_customer)
    app.register_blueprint(delete_customer)
    app.register_blueprint(get_all_accounts)
