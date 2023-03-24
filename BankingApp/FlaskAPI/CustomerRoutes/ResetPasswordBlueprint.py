from datetime import datetime, timedelta

from flask import Blueprint, request, flash, url_for, redirect, current_app, render_template
from flask_mail import Message

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

password_reset = Blueprint("password_reset", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@password_reset.route("/forgot/password", methods=["GET", "POST"])
def request_reset_password():
    mail = current_app.extensions.get("mail")
    if request.method == "POST":
        try:
            email = request.form["resetEmail"]
            customer = customer_sao.service_get_customer_by_email(email)
            if customer is not None:
                session_info = Session(0, customer.customer_id, str(datetime.now() + timedelta(15)))
                session = session_sao.service_create_session(session_info)
                reset_link = url_for("password_reset.change_password", session_id=session.session_id, _external=True)
                message = Message(
                    subject=["Reset Password"],
                    recipients=[customer.email],
                    sender=["no-reply@email.com"])
                message.body = f"Please click the following link to reset your password: {reset_link}"
                mail.send(message)
                flash("An email has been sent with instructions to reset your password", category="success")
            else:
                flash("No account found with that email, please register!")
            return redirect(url_for("login_route.login"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function reset password with error: " + error)
            flash(str(error), category="error")
            return render_template("Customer/ForgotPassword.html")
    else:
        return render_template("Customer/ForgotPassword.html")

@password_reset.route("/change/password/<session_id>", methods=["GET", "POST"])
def change_password(session_id):
    session = session_sao.service_get_session(session_id)
    if session is None:
        flash("The reset password link is invalid or has expired, please request a new one!", category="error")
        return redirect(url_for("password_reset.request_reset_password"))
    else:
        customer = customer_sao.service_get_customer_by_id(session.customer_id)
        if request.method == "POST":
            try:
                password = request.form["resetPassword"]
                password_confirmation = request.form["resetPasswordConfirmation"]
                customer_sao.service_change_password(customer.customer_id, password, password_confirmation)
                session_sao.service_delete_session(session.session_id)
                flash("Your password has been reset, please login with your new password!", category="success")
                return redirect(url_for("login_route.login"))
            except FailedTransaction as error:
                current_app.logger.error("Error with API function change password with error: " + error)
                flash(str(error), category="error")
                return redirect(url_for("Customer/ResetPassword.html", session_id=session_id))
        else:
            return render_template("Customer/ResetPassword.html", session_id=session_id)
