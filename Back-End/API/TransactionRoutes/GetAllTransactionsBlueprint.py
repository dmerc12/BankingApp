from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

get_transactions_route = Blueprint('get_transactions_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@get_transactions_route.route("/get/transactions", methods=["PATCH"])
def view_transactions():
    try:
        session_id = request.json.get("sessionId")
        account_id = request.json.get("accountId")
        current_app.logger.info("Beginning API function view transactions with session ID: " + str(session_id) +
                                ", and account ID: " + str(account_id))
        session_data = session_sao.service_get_session(session_id)
        transactions = transaction_sao.service_get_all_transactions(account_id)
        transaction_list = []
        for transaction in transactions:
            new_transaction = transaction.convert_to_dictionary()
            transaction_list.append(new_transaction)
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        current_app.logger.info("Finishing API function view transactions with result: " + str(transaction_list))
        return jsonify(str(transaction_list)), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function view transactions with error: " + str(error))
        return jsonify({"message": str(error)}), 400
