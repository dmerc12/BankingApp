from flask import Blueprint, request, current_app, flash, redirect, url_for, render_template

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.Entities.Customer import Customer
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.lib.StateCodes import states
from BankingApp.lib.ZipCodes import zip_codes

create_new_customer = Blueprint('create_new_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@create_new_customer.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            customer_info = request.form.to_dict()
            current_app.logger.info("Beginning API function create customer with data: " + str(customer_info))
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
            current_app.logger.info("Finishing API function create customer with result: " + str(result_dictionary))
            flash(message="Account created successfully. Please log in to continue.", category="success")
            return redirect(url_for("login_route.login"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function create customer with error: " + str(error))
            flash(message=str(error), category="error")
            return render_template("Customer/Register.html", states=states, zip_codes=zip_codes)
    else:
        return render_template("Customer/Register.html", states=states, zip_codes=zip_codes)
