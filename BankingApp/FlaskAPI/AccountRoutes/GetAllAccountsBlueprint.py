from flask import jsonify, request, Blueprint, current_app, render_template, url_for, redirect, flash, session

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

@get_relevant_accounts.route("/get/all/accounts", methods=["PATCH"])
def get_all_current_accounts():
    try:
        requested_info: dict = request.get_json()
        current_app.logger.info("Beginning API function get all accounts with data: " + str(requested_info))
        session_id = int(requested_info["sessionId"])
        customer_id = str(session_sao.service_get_session(session_id).customer_id)
        result = account_sao.service_get_all_accounts(customer_id)
        result_dictionary = {
            "accountList": result
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function get all accounts with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message":  str(error)
        }
        current_app.logger.error("Error with API function get all accounts with error: " + str(error))
        return jsonify(message), 400


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
