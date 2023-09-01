from datetime import datetime, timedelta

from flask import Blueprint, current_app, jsonify

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

get_all_accounts_route = Blueprint('get_all_accounts_route', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_all_accounts_route.route("/get/accounts/<int:session_id>", methods=["GET"])
def get_all_accounts_api(session_id):
    try:
        current_app.logger.info("Beginning API function get all accounts with data: " + str(session_id))
        session_data = session_sao.service_get_session(session_id)
        customer_id = session_data.customer_id
        accounts = account_sao.service_get_all_accounts(customer_id)
        account_list = [account.convert_to_dictionary() for account in accounts]
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        current_app.logger.info("Finishing API function get all accounts with result: " + str(account_list))
        return jsonify(account_list), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function get all accounts with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
