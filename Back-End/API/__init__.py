import logging
import os
from flask import Flask
from flask_cors import CORS

from API.CustomerRoutes.LoginBlueprint import login_route
from API.CustomerRoutes.LogoutBlueprint import logout_route
from API.CustomerRoutes.RegisterBlueprint import create_customer_route
from API.CustomerRoutes.UpdateCustomerBlueprint import update_customer_route

def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = os.path.join("Back-End", "Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory,
                            'BankingLogs.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.register_blueprint(login_route)
    app.register_blueprint(logout_route)
    app.register_blueprint(create_customer_route)
    app.register_blueprint(update_customer_route)

    return app
