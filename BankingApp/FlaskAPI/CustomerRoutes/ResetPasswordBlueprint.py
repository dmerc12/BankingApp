from datetime import datetime, timedelta

from flask import Blueprint, request, flash, url_for, redirect, current_app, render_template, app
from flask_mail import Message

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.Database.config import Connect
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
    if request.method == "POST":
        try:
            email = request.form["email"]
            customer = customer_sao.service_get_customer_by_email(email)
            if customer is not None:
                session_info = Session(0, customer.customer_id, str(datetime.now() + timedelta(15)))
                session = session_sao.service_create_session(session_info)
                reset_link = url_for("password_reset.change_password", session_id=session.session_id, _external=True)
                message = Message(
                    subject="Reset Password",
                    recipients=customer.email,
                    body=f"Please click the following link to reset your password: {reset_link}")
                mail = current_app.config.get('mail')
                mail.send()
                flash("An email has been sent with instructions to reset your password", category="success")
            else:
                flash("No account found with that email, please register!")
            return redirect(url_for("login_route.login"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function reset password with error: " + error.message)
            flash(str(error), category="error")
            return render_template("Customer/ForgotPassword.html")
    else:
        return render_template("Customer/ForgotPassword.html")
