from flask import Blueprint, jsonify, request, current_app, session, url_for, redirect, flash, render_template

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

delete_this_account = Blueprint('delete_this_account', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@delete_this_account.route("/delete/account/now", methods=["DELETE"])
def delete_account_now():
    try:
        id_info: dict = request.get_json()
        current_app.logger.info("Beginning API function delete account with data: " + str(id_info))
        session_id = int(id_info["sessionId"])
        account_id = id_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_delete_account(account_id)
        result_json = jsonify(result)
        current_app.logger.info("Finishing API function delete account with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function delete account with error: " + str(error))
        return jsonify(message), 400

@delete_this_account.route("/delete/account", methods=["GET", "POST"])
def delete_account():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        session_id = session["session_id"]
        customer_id = session_sao.service_get_session(session_id).customer_id
        accounts = account_sao.service_get_all_accounts(str(customer_id))
        if request.method == "POST":
            try:
                account_id = request.form["account_id"]
                current_app.logger.info("Beginning API function delete account with data: " + str(session_id) +
                                        ", and " + str(account_id))
                transaction_sao.service_delete_all_transactions(int(account_id))
                result = account_sao.service_delete_account(account_id)
                current_app.logger.info("Finishing API function delete account with result: " + str(result))
                flash(message="Account successfully deleted!", category="success")
                return redirect(url_for("account_routes.manage_accounts"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function delete account with error: " + str(error))
                flash(message=str(error), category="error")
                return render_template("Account/DeleteAccount.html", account_list=accounts)
        else:
            return render_template("Account/DeleteAccount.html", account_list=accounts)
