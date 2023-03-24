import logging
import os

from flask import Flask
from flask_cors import CORS
from flask_mail import Mail

mail = Mail()

def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    # set up the Flask-Mail extension
    app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'flaskbanking@yahoo.com'
    app.config['MAIL_PASSWORD'] = 'Flask123!'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)

    secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = secret_key
    app.jinja_env.filters['floatformat'] = '{:.2f}'.format

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

    from BankingApp.FlaskAPI.AccountRoutes.CreateAccountBlueprint import create_new_account
    from BankingApp.FlaskAPI.AccountRoutes.DeleteAccountBlueprint import delete_this_account
    from BankingApp.FlaskAPI.AccountRoutes.DepositBlueprint import do_deposit
    from BankingApp.FlaskAPI.AccountRoutes.TransferBlueprint import do_transfer
    from BankingApp.FlaskAPI.AccountRoutes.WithdrawBlueprint import do_withdraw
    from BankingApp.FlaskAPI.CustomerRoutes.UpdateCustomerBlueprint import update_customer_blueprint
    from BankingApp.FlaskAPI.MainRoutes.HomeBlueprint import main_route
    from BankingApp.FlaskAPI.MainRoutes.LoginBlueprint import login_route
    from BankingApp.FlaskAPI.CustomerRoutes.CreateCustomerBlueprint import create_new_customer
    from BankingApp.FlaskAPI.MainRoutes.LogoutBlueprint import new_logout
    from BankingApp.FlaskAPI.CustomerRoutes.DeleteCustomerBlueprint import delete_this_customer
    from BankingApp.FlaskAPI.AccountRoutes.GetAllAccountsBlueprint import get_relevant_accounts
    from BankingApp.FlaskAPI.MainRoutes.ManageAccountsBlueprint import account_routes
    from BankingApp.FlaskAPI.CustomerRoutes.ManageCustomerBlueprint import manage_customer_blueprint
    from BankingApp.FlaskAPI.TransactionRoutes.GetAllTransactionsBlueprint import get_relevant_transactions
    from BankingApp.FlaskAPI.CustomerRoutes.ChangePasswordBlueprint import change_password_blueprint
    from BankingApp.FlaskAPI.CustomerRoutes.ResetPasswordBlueprint import password_reset

    app.register_blueprint(create_new_account)
    app.register_blueprint(login_route)
    app.register_blueprint(new_logout)
    app.register_blueprint(create_new_customer)
    app.register_blueprint(delete_this_customer)
    app.register_blueprint(get_relevant_accounts)
    app.register_blueprint(do_deposit)
    app.register_blueprint(do_withdraw)
    app.register_blueprint(do_transfer)
    app.register_blueprint(delete_this_account)
    app.register_blueprint(get_relevant_transactions)
    app.register_blueprint(manage_customer_blueprint)
    app.register_blueprint(account_routes)
    app.register_blueprint(main_route)
    app.register_blueprint(update_customer_blueprint)
    app.register_blueprint(change_password_blueprint)
    app.register_blueprint(password_reset)

    return app
