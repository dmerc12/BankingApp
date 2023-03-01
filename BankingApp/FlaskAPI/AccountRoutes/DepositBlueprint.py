import datetime

from flask import Blueprint, request, current_app, session, flash, url_for, redirect, render_template

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

do_deposit = Blueprint('do_deposit', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@do_deposit.route("/deposit", methods=["GET", "POST"])
def deposit():
    session_id = session["session_id"]
    current_app.logger.info("Beginning API function deposit with data: " + str(session_id))
    customer_id = session_sao.service_get_session(session_id).customer_id
    accounts = account_sao.service_get_all_accounts(str(customer_id))
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        if request.method == "POST":
            try:
                account_id = request.form["account_id"]
                deposit_amount = request.form["amount"]
                deposit_transaction = Transaction(0, str(datetime.datetime.now()), "Deposit", int(account_id),
                                                  float(deposit_amount))
                result = account_sao.service_deposit(account_id, deposit_amount)
                transaction_sao.service_create_transaction(deposit_transaction)
                current_app.logger.info("Finishing API function deposit with result: " + str(result))
                flash("Deposit successful!")
                return redirect(url_for("account_routes.manage_accounts"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function deposit with error: " + str(error))
                flash(str(error))
        else:
            return render_template("Account/Deposit.html", account_list=accounts)
