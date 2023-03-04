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
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        session_id = session["session_id"]
        customer_id = session_sao.service_get_session(session_id).customer_id
        current_customer = customer_sao.service_get_customer_by_id(customer_id)

        if request.method == "POST":
            try:
                updated_info = request.form.to_dict()
                current_app.logger.info("Beginning API function update customer with data: " + str(session_id) +
                                        ", and " + str(updated_info))
                updated_customer = Customer(customer_id=customer_id, first_name=updated_info["updatedFirstName"],
                                            last_name=updated_info["updatedLastName"],
                                            email=updated_info["updatedEmail"],
                                            phone_number=updated_info["updatedPhoneNumber"],
                                            address=updated_info["updatedAddress"], password=current_customer.password)
                result = customer_sao.service_update_customer(updated_customer, customer_id)
                result_dictionary = {
                    "fistName": result.first_name,
                    "lastName": result.last_name,
                    "email": result.email,
                    "phoneNumber": result.phone_number,
                    "address": result.address
                }
                current_app.logger.info("Finishing API functioning update customer with result: " +
                                        str(result_dictionary))
                flash(message="Information successfully updated!", category="success")
                return redirect(url_for("manage_customer_blueprint.manage_customer"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function create customer with error: " + str(error))
                flash(message=str(error), category="error")
                return render_template("Customer/UpdateCustomer.html", current_customer=current_customer)
        else:
            return render_template("Customer/UpdateCustomer.html", current_customer=current_customer)
