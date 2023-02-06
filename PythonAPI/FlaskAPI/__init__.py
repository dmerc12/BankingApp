import logging
import os

from flask import Flask
from flask_cors import CORS

from PythonAPI.FlaskAPI.AccountRoutes.CreateAccountBlueprint import create_new_account
from PythonAPI.FlaskAPI.AccountRoutes.DeleteAccountBlueprint import delete_this_account
from PythonAPI.FlaskAPI.AccountRoutes.DepositBlueprint import do_deposit
from PythonAPI.FlaskAPI.AccountRoutes.TransferBlueprint import do_transfer
from PythonAPI.FlaskAPI.AccountRoutes.WithdrawBlueprint import do_withdraw
from PythonAPI.FlaskAPI.CustomerRoutes.GetCustomerBlueprint import load_customer_info
from PythonAPI.FlaskAPI.CustomerRoutes.LoginBlueprint import new_login
from PythonAPI.FlaskAPI.CustomerRoutes.CreateCustomerBlueprint import create_new_customer
from PythonAPI.FlaskAPI.CustomerRoutes.LogoutBlueprint import new_logout
from PythonAPI.FlaskAPI.CustomerRoutes.UpdateCustomerBlueprint import update_this_customer
from PythonAPI.FlaskAPI.CustomerRoutes.DeleteCustomerBlueprint import delete_this_customer
from PythonAPI.FlaskAPI.AccountRoutes.GetAllAccountsBlueprint import get_relevant_accounts
from PythonAPI.FlaskAPI.TransactionRoutes.GetAllTransactionsBlueprint import get_relevant_transactions

def create_app(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key

    @app.before_request
    def set_up_logs():
        log_level = logging.DEBUG
        for handler in app.logger.handlers:
            app.logger.removeHandler(handler)
        log_directory = "../BankingApp/PythonAPI/Logs"
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)
        log_file = os.path.join("PythonAPI/Logs",
                                'BankingLogs.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)
        app.logger.setLevel(log_level)

    app.register_blueprint(create_new_account)
    app.register_blueprint(new_login)
    app.register_blueprint(new_logout)
    app.register_blueprint(create_new_customer)
    app.register_blueprint(update_this_customer)
    app.register_blueprint(delete_this_customer)
    app.register_blueprint(get_relevant_accounts)
    app.register_blueprint(do_deposit)
    app.register_blueprint(do_withdraw)
    app.register_blueprint(do_transfer)
    app.register_blueprint(delete_this_account)
    app.register_blueprint(get_relevant_transactions)
    app.register_blueprint(load_customer_info)

    return app
