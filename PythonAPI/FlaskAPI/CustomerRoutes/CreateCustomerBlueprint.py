from flask import Blueprint, jsonify, request

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

create_new_customer = Blueprint('create_new_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_new_customer.route("/create/customer", methods=["POST"])
def create_customer():
    try:
        customer_info: dict = request.get_json()
        new_customer = Customer(0, customer_info["firstName"], customer_info["lastName"], customer_info["password"],
                                customer_info["email"], customer_info["phoneNumber"], customer_info["address"])
        password_confirmation = customer_info["passwordConfirmation"]
        result = customer_sao.service_create_customer(new_customer, password_confirmation)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
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
