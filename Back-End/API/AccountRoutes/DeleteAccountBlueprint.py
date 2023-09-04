from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

delete_account_route = Blueprint('delete_account_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@delete_account_route.route("/delete/account", methods=["DELETE"])
def delete_account_api():
    try:
        session_id = request.json.get("sessionId")
        account_id = request.json.get("accountId")
        current_app.logger.info("Beginning API function delete account with data: " + str(session_id) +
                                ", and " + str(account_id))
        session_data = session_sao.service_get_session(session_id)
        transaction_sao.service_delete_all_transactions(account_id)
        result = account_sao.service_delete_account(account_id)
        current_app.logger.info("Finishing API function delete account with result: " + str(result))
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(result), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function delete account with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
