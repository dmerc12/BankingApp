import datetime

from flask import Blueprint, request, current_app, render_template, url_for, redirect, session, flash

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

do_withdraw = Blueprint('do_withdraw', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@do_withdraw.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        try:
            session_id = session["session_id"]
            customer_id = session_sao.service_get_session(session_id).customer_id
            accounts = account_sao.service_get_all_accounts(str(customer_id))
            if request.method == "POST":
                try:
                    account_id = request.form["account_id"]
                    withdraw_amount = request.form["amount"]
                    current_app.logger.info("Beginning API function withdraw with data: " + str(session_id) + ", and "
                                            + str(account_id) + ", and " + str(withdraw_amount))
                    withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "Withdraw", int(account_id),
                                                       float(withdraw_amount))
                    result = account_sao.service_withdraw(account_id, withdraw_amount)
                    transaction_sao.service_create_transaction(withdraw_transaction)
                    current_app.logger.info("Finishing API function withdraw with result: " + str(result))
                    flash(message="Withdraw successful!", category="success")
                    return redirect(url_for("account_routes.manage_accounts"))
                except FailedTransaction as error:
                    current_app.logger.error("Error with API function withdraw with error: " + str(error))
                    flash(message=str(error), category="error")
                    return render_template("Account/Withdraw.html", account_list=accounts)

            else:
                return render_template("Account/Withdraw.html", account_list=accounts)
        except FailedTransaction as error:
            current_app.logger.error("Error with API function withdraw with error: " + str(error))
            flash(message=str(error), category="error")
            return redirect(url_for("account_routes.manage_accounts"))
