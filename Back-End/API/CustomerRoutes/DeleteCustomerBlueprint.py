from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app, session

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

delete_customer_route = Blueprint("delete_customer_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

@delete_customer_route.route("/delete/customer/now", methods=["DELETE"])
def delete_customer_api():
    try:
        session_id = request.json.get("sessionId")
        session_data = session_sao.service_get_session(session_id)
        customer_id = session_data.customer_id
        current_app.logger.info("Beginning API function delete customer with session ID: " + str(session_id) +
                                ", and customer ID: " + str(customer_id))
        session_sao.service_delete_all_sessions(customer_id)
        account_sao.service_delete_all_accounts(customer_id)
        result = customer_sao.service_delete_customer(customer_id)
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session_data.expire_date_time = new_expire_date_time
        session_dao.update_session(session_data)
        current_app.logger.info("Finishing API function delete customer")
        response = {
            "message": str(result)
        }
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function delete customer with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
