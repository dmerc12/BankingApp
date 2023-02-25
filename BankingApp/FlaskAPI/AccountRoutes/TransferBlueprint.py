import datetime

from flask import Blueprint, request, jsonify, current_app, session, flash, redirect, url_for, render_template

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

@do_transfer.route("/make/transfer", methods=["PATCH"])
def make_transfer():
    try:
        transfer_info: dict = request.get_json()
        current_app.logger.info("Beginning API function transfer with data: " + str(transfer_info))
        session_id = int(transfer_info["sessionId"])
        session_sao.service_get_session(session_id)
        transfer_amount = transfer_info["transferAmount"]
        withdraw_account_id = transfer_info["withdrawAccountId"]
        deposit_account_id = transfer_info["depositAccountId"]
        result = account_sao.service_transfer(withdraw_account_id, deposit_account_id, transfer_amount)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        withdraw_transaction_account_id = withdraw_account_id
        withdraw_transaction_amount = transfer_amount
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw",
                                           int(withdraw_transaction_account_id), float(withdraw_transaction_amount))
        transaction_sao.service_create_transaction(withdraw_transaction)
        deposit_transaction_account_id = deposit_account_id
        deposit_transaction_amount = transfer_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit",
                                          int(deposit_transaction_account_id), float(deposit_transaction_amount))
        transaction_sao.service_create_transaction(deposit_transaction)
        current_app.logger.info("Finishing API function transfer with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function transfer with data: " + str(error))
        return jsonify(message), 400


@do_transfer.route("/transfer", methods=["GET"])
def transfer():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        return render_template("Account/Transfer.html")
