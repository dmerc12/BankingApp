import logging
import os

from flask import Flask
from flask_cors import CORS

from BankingApp.FlaskAPI.AccountRoutes.CreateAccountBlueprint import create_new_account
from BankingApp.FlaskAPI.AccountRoutes.DeleteAccountBlueprint import delete_this_account
from BankingApp.FlaskAPI.AccountRoutes.DepositBlueprint import do_deposit
from BankingApp.FlaskAPI.AccountRoutes.TransferBlueprint import do_transfer
from BankingApp.FlaskAPI.AccountRoutes.WithdrawBlueprint import do_withdraw
from BankingApp.FlaskAPI.CustomerRoutes.GetCustomerBlueprint import load_customer_info
from BankingApp.FlaskAPI.MainRoutes.HomeBlueprint import main_route
from BankingApp.FlaskAPI.MainRoutes.LoginBlueprint import login_route
from BankingApp.FlaskAPI.CustomerRoutes.CreateCustomerBlueprint import create_new_customer
from BankingApp.FlaskAPI.MainRoutes.LogoutBlueprint import new_logout
from BankingApp.FlaskAPI.CustomerRoutes.UpdateCustomerBlueprint import update_this_customer
from BankingApp.FlaskAPI.CustomerRoutes.DeleteCustomerBlueprint import delete_this_customer
from BankingApp.FlaskAPI.AccountRoutes.GetAllAccountsBlueprint import get_relevant_accounts
from BankingApp.FlaskAPI.MainRoutes.AccountRoutes import account_routes
from BankingApp.FlaskAPI.CustomerRoutes.ManageCustomerBlueprint import manage_customer_blueprint
from BankingApp.FlaskAPI.TransactionRoutes.TransactionRoutes import transaction_routes
from BankingApp.FlaskAPI.TransactionRoutes.GetAllTransactionsBlueprint import get_relevant_transactions

def create_back_end_api(config):
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
        log_directory = "../BankingApp/BankingApp/Logs"
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)
        log_file = os.path.join("BankingApp/Logs",
                                'BankingLogs.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)
        app.logger.setLevel(log_level)

    app.register_blueprint(create_new_account)
    app.register_blueprint(login_route)
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
    app.register_blueprint(manage_customer_blueprint)
    app.register_blueprint(account_routes)
    app.register_blueprint(transaction_routes)
    app.register_blueprint(main_route)

    return app