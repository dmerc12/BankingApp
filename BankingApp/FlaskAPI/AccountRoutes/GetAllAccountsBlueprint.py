from flask import Blueprint, current_app, render_template, url_for, redirect, flash, session

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
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
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        session_id = session["session_id"]
        current_app.logger.info("Beginning API function get all accounts with data: " + str(session_id))
        customer_id = str(session_sao.service_get_session(session_id).customer_id)
        accounts = account_sao.service_get_all_accounts(customer_id)
        current_app.logger.info("Finishing API function get all accounts with result: " + str(accounts))
        return render_template("Account/ViewAllAccounts.html", account_list=accounts)
