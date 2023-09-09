from flask import Blueprint, request, current_app, jsonify

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

create_customer_route = Blueprint('create_customer_route', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_customer_route.route("/register/now", methods=["POST"])
def register():
    try:
        customer_info = request.json
        if not customer_info:
            response = {
                "message": "Invalid request format"
            }
            return jsonify(response), 400
        current_app.logger.info("Beginning API function create customer with data: " + str(customer_info))
        new_customer = Customer(0, customer_info["firstName"], customer_info["lastName"],
                                customer_info["password"], customer_info["email"],
                                customer_info["phoneNumber"], customer_info["address"])
        password_confirmation = customer_info["passwordConfirmation"]
        result = customer_sao.service_create_customer(new_customer, password_confirmation)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        current_app.logger.info("Finishing API function create customer with result: " + str(result_dictionary))
        return jsonify(result_dictionary), 201
    except FailedTransaction as error:
        current_app.logger.error("Error with API function create customer with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400

