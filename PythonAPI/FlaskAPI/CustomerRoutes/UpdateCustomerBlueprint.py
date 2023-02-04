from flask import Blueprint, jsonify, request

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

update_this_customer = Blueprint('update_this_customer', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@update_this_customer.route("/update/customer", methods=["PATCH"])
def update_customer():
    try:
        new_customer_information: dict = request.get_json()
        session_id = int(new_customer_information["sessionId"])
        current_customer_id = session_sao.service_get_session(session_id).customer_id
        updated_customer_information = Customer(current_customer_id,
                                                new_customer_information["firstName"],
                                                new_customer_information["lastName"],
                                                new_customer_information["username"],
                                                new_customer_information["password"],
                                                new_customer_information["email"],
                                                new_customer_information["phoneNumber"],
                                                new_customer_information["address"])
        result = customer_sao.service_update_customer(updated_customer_information)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
            "username": result.username,
            "password": result.password,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
