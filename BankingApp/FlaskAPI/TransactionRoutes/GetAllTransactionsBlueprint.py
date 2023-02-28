from flask import Blueprint, jsonify, request, current_app, session, flash, url_for, redirect, render_template

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


@get_relevant_transactions.route("/get/all/transactions", methods=["PATCH"])
def get_all_transactions():
    try:
        id_info: dict = request.get_json()
        current_app.logger.info("Beginning API function get all transactions with data: " + str(id_info))
        session_id = int(id_info["sessionId"])
        account_id = int(id_info["accountId"])
        session_sao.service_get_session(session_id)
        result = transaction_sao.service_get_all_transactions(account_id)
        result_dictionary = {
            "transactionList": result
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function get all transactions with resulting information: "
                                + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function get all transactions with message: " + str(error))
        return jsonify(message), 400

@get_relevant_transactions.route("/account/<int:account_id>/transactions", methods=["GET"])
def view_transactions(account_id):
    session_id = session.get('session_id')
    current_app.logger.info("Beginning API function view transactions with data: " + str(session_id) + ", and " +
                            str(account_id))
    session_verification = session_sao.service_get_session(session_id)
    if session_id is None:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        try:
            account = account_sao.service_get_account_by_id(account_id)
            if account.customer_id != session_verification.customer_id:
                flash("You are not authorized to view this account!")
                return redirect(url_for("account_routes.manage_accounts"))
            else:
                transactions = transaction_sao.service_get_all_transactions(account_id)
                current_app.logger.info("Finishing API function view transactions with result: " + str(transactions))
                return render_template("Transaction/Transactions.html", account=account, transactions=transactions)
        except FailedTransaction as error:
            current_app.logger.error("Error with API function view transactions with error: " + str(error))
            flash("Error viewing transactions: " + str(error))
            return redirect(url_for("account_routes.manage_accounts"))
