import datetime

from flask import Blueprint, render_template, request, jsonify, current_app, make_response, redirect, url_for, flash, \
    session

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Customer import Customer
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

customer_routes = Blueprint("customer_routes", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@customer_routes.route("/manage/customer", methods=["GET"])
def manage_customer():
    return render_template("Customer/ManageCustomer.html")

@customer_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle form submission for new customer registration
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
            flash("Account created successfully. Please log in to continue.")
            return redirect(url_for("login_route.login"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function create customer with error: " + str(error))
            flash(str(error))
    # Render registration form
    return render_template("Customer/Register.html")