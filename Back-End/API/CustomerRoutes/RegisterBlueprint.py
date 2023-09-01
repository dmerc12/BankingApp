from flask import Blueprint, request, current_app, jsonify

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

create_customer = Blueprint('create_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_customer.route("/register-now", methods=["POST"])
def register():
    try:
        customer_info = request.json
        if not customer_info:
            response = {
                "message": "Invalid request format"
            }
            return jsonify(response), 400
        current_app.logger.info("Beginning API function create customer with data: " + str(customer_info))
        street_address = customer_info["registerStreetAddress"]
        city = customer_info["registerCity"]
        state = customer_info["registerState"]
        zip_code = customer_info["registerZipCode"]
        full_address = f"{street_address}, {city}, {state} {zip_code}"
        new_customer = Customer(0, customer_info["registerFirstName"], customer_info["registerLastName"],
                                customer_info["registerPassword"], customer_info["registerEmail"],
                                customer_info["registerPhoneNumber"], full_address)
        password_confirmation = customer_info["registerPasswordConfirmation"]
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

