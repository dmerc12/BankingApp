import datetime

from flask import Blueprint, jsonify, request, current_app

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

do_deposit = Blueprint('do_deposit', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@do_deposit.route("/deposit", methods=["PATCH"])
def deposit():
    try:
        deposit_info: dict = request.get_json()
        current_app.logger.info("Beginning API function deposit with data: " + str(deposit_info))
        session_id = int(deposit_info["sessionId"])
        deposit_amount = deposit_info["depositAmount"]
        account_id = deposit_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_deposit(account_id, deposit_amount)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = deposit_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", int(transaction_account_id),
                                          float(transaction_amount))
        transaction_sao.service_create_transaction(deposit_transaction)
        current_app.logger.info("Finishing API function deposit with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function deposit with error: " + str(error))
        return jsonify(message), 400