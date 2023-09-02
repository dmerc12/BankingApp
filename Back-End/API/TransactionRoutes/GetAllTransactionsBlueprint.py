from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

get_all_transactions = Blueprint('get_all_transactions', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@get_all_transactions.route("/get/transactions/<int:session_id>/<int:account_id>", methods=["GET"])
def view_transactions(session_id, account_id):
    try:
        current_app.logger.info("Beginning API function view transactions with data: " + str(session_id) + ", and " +
                                str(account_id))
        session_data = session_sao.service_get_session(session_id)
        transactions = transaction_sao.service_get_all_transactions(account_id)
        current_app.logger.info("Finishing API function view transactions with result: " + str(transactions))
        response = [{"transaction_id": transaction.transaction_id,
                     "date_time": transaction.date_time,
                     "transaction_type": transaction.transaction_type,
                     "account_id": transaction.account_id,
                     "amount": transaction.amount} for transaction in transactions]
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function view transactions with error: " + str(error))
        return jsonify({"message": str(error)}), 400
