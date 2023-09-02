from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

update_customer_route = Blueprint("update_customer_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_customer_route.route("/update/customer/now", methods=["PUT"])
def update_customer():
    try:
        updated_info = request.json
        session_id = updated_info["sessionId"]
        current_customer = customer_sao.service_get_customer_by_id(session_id)
        current_app.logger.info("Beginning API function update customer with data: " + str(updated_info))
        updated_customer = Customer(customer_id=current_customer.customer_id, first_name=updated_info["firstName"],
                                    last_name=updated_info["lastName"],
                                    email=updated_info["email"],
                                    phone_number=updated_info["phoneNumber"],
                                    address=updated_info["address"], password=current_customer.password)
        result = customer_sao.service_update_customer(updated_customer, current_customer.customer_id)
        current_session = session_sao.service_get_session(session_id)
        updated_session_time = datetime.now() + timedelta(minutes=15)
        current_session.expire_date_time = updated_session_time
        session_dao.update_session(current_session)
        result_dictionary = {
            "fistName": result.first_name,
            "lastName": result.last_name,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        current_app.logger.info("Finishing API functioning update customer with result: " +
                                str(result_dictionary))
        return jsonify(result_dictionary), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function create customer with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
