from flask import Blueprint, jsonify, request

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

create_customer = Blueprint('create_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_customer.route("/create/customer", methods=["POST"])
def create_customer():
    try:
        customer_info: dict = request.get_json()
        new_customer = Customer(0, customer_info["firstName"], customer_info["lastName"], customer_info["username"],
                                customer_info["password"], customer_info["email"], customer_info["phoneNumber"],
                                customer_info["address"])
        result = customer_sao.service_create_customer(new_customer)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
