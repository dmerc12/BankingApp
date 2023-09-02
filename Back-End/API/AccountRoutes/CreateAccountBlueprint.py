from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.BankAccount import BankAccount
from Entities.FailedTransaction import FailedTransaction
from Entities.Transaction import Transaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

create_account_route = Blueprint('create_account_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@create_account_route.route("/create/account", methods=["POST"])
def create_account_api():
    try:
        session_id = request.json.get("sessionId")
        starting_balance = request.json.get("startingBalance")
        session_data = session_sao.service_get_session(session_id)
        customer_id = session_data.customer_id
        current_app.logger.info("Beginning API function create new account with data: " + str(session_id)
                                + ", and " + str(starting_balance))
        starting_balance = float(starting_balance)
        new_account = BankAccount(0, customer_id, starting_balance)
        result = account_sao.service_create_account(new_account)
        account_creation_transaction = Transaction(0, str(datetime.now()), "Account Created",
                                                   int(new_account.account_id), starting_balance)
        transaction_sao.service_create_transaction(account_creation_transaction)
        response = {
            "accountId": result.account_id,
            "startingBalance": result.balance
        }
        current_app.logger.info("Finishing API function create new account with result: " +
                                str(response))
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function create new account with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
