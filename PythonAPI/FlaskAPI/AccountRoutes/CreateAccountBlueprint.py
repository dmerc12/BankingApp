import datetime
from flask import Blueprint, jsonify, request

from PythonAPI.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from PythonAPI.Entities.BankAccount import BankAccount
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.Entities.Transaction import Transaction
from PythonAPI.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from PythonAPI.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

Account = Blueprint('Account', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@Account.route("/create/account", methods=["POST"])
def create_account():
    try:
        account_data: dict = request.get_json()
        session_id = int(account_data["sessionId"])
        balance = float(account_data["balance"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        new_account: BankAccount = BankAccount(0, customer_id,
                                               balance)
        result = account_sao.service_create_account(new_account)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = result.account_id
        transaction_amount = result.balance
        setup_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", transaction_account_id,
                                        transaction_amount)
        transaction_sao.service_create_transaction(setup_transaction)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400

