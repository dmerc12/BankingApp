from flask import Blueprint, jsonify, request, current_app, session, redirect, url_for, flash, render_template

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

delete_this_customer = Blueprint('delete_this_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_this_customer.route("/delete/my/information", methods=["DELETE"])
def delete_my_information():
    try:
        requested_info = request.get_json()
        current_app.logger.info("Beginning API function delete customer with data: " + str(requested_info))
        session_id = int(requested_info["sessionId"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        session_sao.service_delete_all_sessions(customer_id)
        result = customer_sao.service_delete_customer(customer_id)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function delete customer with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Finishing API function delete customer with error: " + str(error))
        return jsonify(message), 400


@delete_this_customer.route("/delete/customer", methods=["GET", "POST"])
def delete_customer():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        session_id = session["session_id"]
        customer_id = session_sao.service_get_session(session_id).customer_id

        if request.method == "POST":
            try:
                current_app.logger.info("Beginning API function delete customer with data: " + str(session_id) +
                                        ", and " + str(customer_id))
                session_sao.service_delete_all_sessions(customer_id)
                result = customer_sao.service_delete_customer(customer_id)
                current_app.logger.info("Finishing API function delete customer with result: " + str(result))
                flash(message="Information successfully deleted!", category="success")
                return redirect(url_for("login_route.login"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function delete customer with error: " + str(error))
                flash(message=str(error), category="error")
                return render_template("Customer/DeleteCustomer.html")
        else:
            return render_template("Customer/DeleteCustomer.html")
