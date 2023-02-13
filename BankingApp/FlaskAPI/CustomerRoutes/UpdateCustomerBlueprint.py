from flask import Blueprint, jsonify, request, current_app

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Customer import Customer
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

update_this_customer = Blueprint('update_this_customer', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@update_this_customer.route("/update/customer", methods=["PATCH"])
def update_customer():
    try:
        new_customer_information: dict = request.get_json()
        current_app.logger.info("Beginning API function update customer with data: " + str(new_customer_information))
        session_id = int(new_customer_information["sessionId"])
        current_customer_id = session_sao.service_get_session(session_id).customer_id
        updated_customer_information = Customer(current_customer_id,
                                                new_customer_information["firstName"],
                                                new_customer_information["lastName"],
                                                new_customer_information["password"],
                                                new_customer_information["email"],
                                                new_customer_information["phoneNumber"],
                                                new_customer_information["address"])
        result = customer_sao.service_update_customer(updated_customer_information)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function update customer with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function update customer with data: " + str(error))
        return jsonify(message), 400
