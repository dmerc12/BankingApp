import datetime
from flask import Blueprint, jsonify, request, current_app, session, flash, redirect, render_template, url_for

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.BankAccount import BankAccount
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

create_new_account = Blueprint('create_new_account', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@create_new_account.route("/create/account/now", methods=["POST"])
def create_account_now():
    try:
        account_data: dict = request.get_json()
        current_app.logger.info("Beginning API function create account with data: " + str(account_data))
        session_id = int(account_data["sessionId"])
        balance = float(account_data["balance"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        new_account: BankAccount = BankAccount(0, customer_id,
                                               balance)
        result = account_sao.service_create_account(new_account)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = result.account_id
        transaction_amount = result.balance
        setup_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", transaction_account_id,
                                        transaction_amount)
        transaction_sao.service_create_transaction(setup_transaction)
        current_app.logger.info("Finishing API function create account with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function create account with error: " + str(error))
        return jsonify(message), 400

@create_new_account.route("/create/account", methods=["GET", "POST"])
def create_account():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        if request.method == "POST":
            try:
                session_id = session["session_id"]
                starting_balance = float(request.form.to_dict()["startingBalance"])
                current_app.logger.info("Beginning API function create new account with data: " + str(session_id)
                                        + ", and " + str(starting_balance))
                customer_id = session_sao.service_get_session(session_id).customer_id
                new_account = BankAccount(0, customer_id, starting_balance)
                result = account_sao.service_create_account(new_account)
                result_dictionary = {
                    "accountId": result.account_id,
                    "startingBalance": result.balance
                }
                current_app.logger.info("Finishing API function create new account with result: " +
                                        str(result_dictionary))
                flash("Account successfully created!")
                return redirect(url_for("account_routes.manage_accounts"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function create new account with error: " + str(error))
                flash(str(error))
        else:
            return render_template("Account/CreateAccount.html")
