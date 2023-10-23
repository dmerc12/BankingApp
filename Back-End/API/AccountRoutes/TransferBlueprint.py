from datetime import datetime, timedelta

from flask import Blueprint, request, current_app, jsonify

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

transfer_route = Blueprint('transfer_route', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@transfer_route.route("/api/transfer", methods=["PUT"])
def transfer_api():
    try:
        current_app.logger.info("Beginning API function transfer with data: " + str(request.json))
        session_id = request.json.get("sessionId")
        withdraw_account_id = request.json.get("withdrawAccountId")
        deposit_account_id = request.json.get("depositAccountId")
        transfer_amount = request.json.get("transferAmount")
        session_data = session_sao.service_get_session(session_id)
        result = account_sao.service_transfer(withdraw_account_id, deposit_account_id, transfer_amount)
        current_app.logger.info("Finishing API function transfer with result: " + str(result))
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(result), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function transfer with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
