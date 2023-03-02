import datetime

from flask import Blueprint, request, current_app, session, flash, redirect, url_for, render_template

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

do_transfer = Blueprint('do_transfer', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@do_transfer.route("/transfer", methods=["GET", "POST"])
def transfer():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        session_id = session["session_id"]
        customer_id = session_sao.service_get_session(session_id).customer_id
        accounts = account_sao.service_get_all_accounts(str(customer_id))
        if request.method == "POST":
            try:
                withdraw_account_id = request.form["withdraw_account_id"]
                deposit_account_id = request.form["deposit_account_id"]
                transfer_amount = request.form["amount"]
                current_app.logger.info("Beginning PI function transfer with data: " + str(session_id) + ", and " +
                                        str(withdraw_account_id) + ", and " + str(deposit_account_id) + ", and " +
                                        str(transfer_amount))
                withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "Withdraw", int(withdraw_account_id),
                                                   float(transfer_amount))
                deposit_transaction = Transaction(0, str(datetime.datetime.now()), "Deposit", int(deposit_account_id),
                                                  float(transfer_amount))
                result = account_sao.service_transfer(withdraw_account_id, deposit_account_id, transfer_amount)
                transaction_sao.service_create_transaction(withdraw_transaction)
                transaction_sao.service_create_transaction(deposit_transaction)
                current_app.logger.info("Finishing API function transfer with result: " + str(result))
                flash(message="Transfer successful!", category="success")
                return redirect(url_for("account_routes.manage_accounts"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function transfer with error: " + str(error))
                flash(message=str(error), category="error")
                return render_template("Account/Transfer.html", account_list=accounts)
        else:
            return render_template("Account/Transfer.html", account_list=accounts)
