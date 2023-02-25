from flask import Blueprint, render_template, redirect, url_for, flash, session, request, current_app

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Customer import Customer
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

update_customer_blueprint = Blueprint("update_customer_blueprint", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_customer_blueprint.route("/update/customer", methods=["POST", "GET"])
def update_customer():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        if request.method == "POST":
            try:
                session_id = session["session_id"]
                updated_info = request.form.to_dict()
                current_app.logger.info("Beginning API function update customer with data: " + str(session_id) +
                                        ", and " + str(updated_info))
                customer_id = session_sao.service_get_session(session_id).customer_id
                updated_customer = Customer(customer_id, updated_info["updatedFirstName"],
                                            updated_info["updatedLastName"], updated_info["updatedEmail"],
                                            updated_info["updatedPassword"], updated_info["updatedPhoneNumber"],
                                            updated_info["updatedAddress"])
                result = customer_sao.service_update_customer(updated_customer,
                                                              updated_info["updatedPasswordConfirmation"])
                result_dictionary = {
                    "fistName": result.first_name,
                    "lastName": result.last_name,
                    "email": result.email,
                    "phoneNumber": result.phone_number,
                    "address": result.address
                }
                current_app.logger.info("Finishing API functioning update customer with result: " +
                                        str(result_dictionary))
                flash("Information successfully updated!")
                return redirect(url_for("manage_customer_blueprint.manage_customer"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function create customer with error: " + str(error))
                flash(str(error))
        else:
            return render_template("Customer/UpdateCustomer.html")
