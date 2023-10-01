from flask import Blueprint, request, current_app, jsonify
from datetime import datetime, timedelta

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

withdraw_route = Blueprint('withdraw_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@withdraw_route.route("/withdraw", methods=["PUT"])
def withdraw_api():
    try:
        current_app.logger.info("Beginning API function withdraw with session ID: " + str(request.json))
        session_id = request.json.get("sessionId")
        account_id = request.json.get("accountId")
        withdraw_amount = request.json.get("withdrawAmount")
        session_data = session_sao.service_get_session(session_id)
        result = account_sao.service_withdraw(account_id, withdraw_amount)
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        result_dictionary = result.convert_to_dictionary()
        current_app.logger.info("Finishing API function withdraw with result: " + str(result_dictionary))
        return jsonify(result_dictionary), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function withdraw with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
