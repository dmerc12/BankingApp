import datetime

from flask import Blueprint, jsonify, request

from PythonAPI.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.Entities.Transaction import Transaction
from PythonAPI.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from PythonAPI.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

deposit = Blueprint('deposit', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@deposit.route("/deposit", methods=["PATCH"])
def deposit():
    try:
        deposit_info: dict = request.get_json()
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
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
