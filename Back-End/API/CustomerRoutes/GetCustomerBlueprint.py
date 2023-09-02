from datetime import datetime, timedelta

from flask import Blueprint, jsonify, current_app, request

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

get_customer_route = Blueprint('get_customer_route', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_customer_route.route("/get/customer/now", methods=["PATCH"])
def get_customer():
    try:
        session_id = request.json.get("sessionId")
        current_app.logger.info("Beginning API function get customer with data: " + str(session_id))
        current_customer_id = session_sao.service_get_session(session_id).customer_id
        current_customer = customer_sao.service_get_customer_by_id(current_customer_id)
        current_session = session_sao.service_get_session(session_id)
        updated_session_time = datetime.now() + timedelta(minutes=15)
        current_session.expire_date_time = updated_session_time
        session_dao.update_session(current_session)
        customer_dictionary = {
            "firstName": current_customer.first_name,
            "lastName": current_customer.last_name,
            "email": current_customer.email,
            "phoneNumber": current_customer.phone_number,
            "address": current_customer.address
        }
        current_app.logger.info("Finishing API function get customer with result: " + str(customer_dictionary))
        return jsonify(customer_dictionary), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function get customer with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
