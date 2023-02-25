import datetime

from flask import Blueprint, request, jsonify, current_app, render_template, url_for, redirect, session, flash

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

@do_withdraw.route("/make/withdraw", methods=["PATCH"])
def make_withdraw():
    try:
        withdraw_info: dict = request.get_json()
        current_app.logger.info("Beginning API function withdraw with data: " + str(withdraw_info))
        session_id = int(withdraw_info["sessionId"])
        withdraw_amount = withdraw_info["withdrawAmount"]
        account_id = withdraw_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_withdraw(account_id, withdraw_amount)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = withdraw_amount
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw", int(transaction_account_id),
                                           float(transaction_amount))
        transaction_sao.service_create_transaction(withdraw_transaction)
        current_app.logger.info("Finishing API function withdraw with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function withdraw with error: " + str(error))
        return jsonify(message), 400


@do_withdraw.route("/withdraw", methods=["GET"])
def withdraw():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        return render_template("Account/Withdraw.html")
