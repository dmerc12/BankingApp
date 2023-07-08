from flask import Blueprint, request, current_app, flash, redirect, url_for, render_template

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.Entities.Customer import Customer
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.LocationData.StateCodes import states
from BankingApp.LocationData.ZipCodes import zip_codes

create_new_customer = Blueprint('create_new_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_new_customer.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            customer_info = request.form.to_dict()
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
            flash(message="Account created successfully. Please log in to continue.", category="success")
            return redirect(url_for("login_route.login"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function create customer with error: " + str(error))
            flash(message=str(error), category="error")
            return render_template("Customer/Register.html", states=states, zip_codes=zip_codes)
    else:
        return render_template("Customer/Register.html", states=states, zip_codes=zip_codes)
