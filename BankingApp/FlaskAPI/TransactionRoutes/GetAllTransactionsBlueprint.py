from flask import Blueprint, current_app, session, flash, url_for, redirect, render_template

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

get_relevant_transactions = Blueprint('get_relevant_transactions', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@get_relevant_transactions.route("/account/<account_id>/transactions", methods=["GET"])
def view_transactions(account_id):
    session_id = session.get('session_id')
    session_verification = session_sao.service_get_session(session_id)
    if session_id is None:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        current_app.logger.info("Beginning API function view transactions with data: " + str(session_id) + ", and " +
                                str(account_id))
        try:
            account = account_sao.service_get_account_by_id(account_id)
            if account.customer_id != session_verification.customer_id:
                flash("You are not authorized to view this account!")
                return redirect(url_for("account_routes.manage_accounts"))
            else:
                transactions = transaction_sao.service_get_all_transactions(account_id)
                current_app.logger.info("Finishing API function view transactions with result: " + str(transactions))
                return render_template("Transaction/Transactions.html", transaction_list=transactions)
        except FailedTransaction as error:
            current_app.logger.error("Error with API function view transactions with error: " + str(error))
            flash("Error viewing transactions: " + str(error))
            return redirect(url_for("account_routes.manage_accounts"))
