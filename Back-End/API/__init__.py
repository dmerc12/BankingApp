import logging
import os
from flask import Flask
from flask_cors import CORS

from API.CustomerRoutes.LoginBlueprint import login_route
from API.CustomerRoutes.LogoutBlueprint import logout_route
from API.CustomerRoutes.RegisterBlueprint import create_customer


def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    @app.before_request
    def set_up_logs():
        log_level = logging.DEBUG
        for handler in app.logger.handlers:
            app.logger.removeHandler(handler)
        log_directory = "../BankingApp/BankingApp/Logs"
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)
        log_file = os.path.join("BankingApp/Logs",
                                'BankingLogs.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)
        app.logger.setLevel(log_level)

    app.register_blueprint(login_route)
    app.register_blueprint(logout_route)
    app.register_blueprint(create_customer)

    return app
