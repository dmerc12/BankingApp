from flask import Blueprint, current_app, render_template, url_for, redirect, flash, session

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

get_relevant_accounts = Blueprint('get_relevant_accounts', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_relevant_accounts.route("/get/accounts", methods=["GET"])
def get_all_accounts():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        try:
            session_id = session["session_id"]
            current_app.logger.info("Beginning API function get all accounts with data: " + str(session_id))
            customer_id = str(session_sao.service_get_session(session_id).customer_id)
            accounts = account_sao.service_get_all_accounts(customer_id)
            for account in accounts:
                current_app.logger.info("Finishing API function get all accounts with result: " +
                                        str(account.convert_to_dictionary()))
            return render_template("Account/ViewAllAccounts.html", account_list=accounts)
        except FailedTransaction as error:
            current_app.logger.error("Error with API function get all accounts with error: " + str(error))
            flash(message=str(error), category="error")
            return redirect(url_for("account_routes.manage_accounts"))
