from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.BankAccount import BankAccount
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

create_account_route = Blueprint('create_account_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@create_account_route.route("/api/create/account", methods=["POST"])
def create_account_api():
    try:
        current_app.logger.info("Beginning API function create new account with data: " + str(request.json))
        session_id = request.json.get("sessionId")
        starting_balance = float(request.json.get("startingBalance"))
        session_data = session_sao.service_get_session(session_id)
        customer_id = session_data.customer_id
        new_account = BankAccount(0, customer_id, starting_balance)
        result = account_sao.service_create_account(new_account)
        response = {
            "accountId": result.account_id,
            "startingBalance": result.balance
        }
        current_app.logger.info("Finishing API function create new account with result: " +
                                str(response))
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        return jsonify(response), 201
    except FailedTransaction as error:
        current_app.logger.error("Error with API function create new account with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
