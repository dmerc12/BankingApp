from flask import Blueprint, request, current_app, jsonify
from datetime import datetime, timedelta

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from Entities.Transaction import Transaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

withdraw_route = Blueprint('withdraw_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@withdraw_route.route("/withdraw/now", methods=["PUT"])
def withdraw_api():
    try:
        session_id = request.json.get("sessionId")
        account_id = request.json.get("withdrawAccountId")
        withdraw_amount = request.json.get("withdrawAmount")
        session_data = session_sao.service_get_session(session_id)
        current_app.logger.info("Beginning API function withdraw with session ID: " + str(session_id) +
                                ", and account ID: " + str(account_id) + ", and withdraw amount:" + str(withdraw_amount))
        account_id = int(account_id)
        withdraw_amount = float(withdraw_amount)
        withdraw_transaction = Transaction(0, str(datetime.now()), "Withdraw", account_id, withdraw_amount)
        result = account_sao.service_withdraw(account_id, withdraw_amount)
        transaction_sao.service_create_transaction(withdraw_transaction)
        current_app.logger.info("Finishing API function withdraw with result: " + str(result))
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(result), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function withdraw with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
