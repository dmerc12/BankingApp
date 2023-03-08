from flask import Blueprint, session, flash, redirect, url_for, request, current_app, render_template

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

change_password_blueprint = Blueprint("change_password_blueprint", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@change_password_blueprint.route("/change/password", methods=["POST", "GET"])
def change_password():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        if request.method == "POST":
            try:
                session_id = session["session_id"]
                customer_id = session_sao.service_get_session(session_id).customer_id
                new_password = request.form["newPassword"]
                confirmation_password = request.form["confirmationPassword"]
                current_app.logger.info("Beginning API function change password with customer ID: " + str(customer_id)
                                        + ", new password: " + new_password + ", confirmation password: " +
                                        confirmation_password)
                customer_sao.service_change_password(customer_id, new_password, confirmation_password)
                current_app.logger.info("Finishing API function change password")
                flash(message="Password successfully updated!", category="success")
                return redirect(url_for("manage_customer_blueprint.manage_customer"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function change password with error: " + str(error))
                flash(message=str(error), category="error")
                return render_template("Customer/ChangePassword.html", error=error)
        else:
            return render_template("Customer/ChangePassword.html")
