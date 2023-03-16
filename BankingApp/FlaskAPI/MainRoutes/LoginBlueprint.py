import datetime

from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, session

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

login_route = Blueprint("login_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@login_route.route("/", methods=["GET", "POST"])
@login_route.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]
            current_app.logger.info("Beginning API function login with data: " + str(email) + ", " + str(password))

            result = customer_sao.service_login(email, password)
            new_session_info = Session(0, result.customer_id, str(datetime.datetime.now() +
                                                                  datetime.timedelta(0, 0, 0, 0, 0, 1)))
            new_session = session_sao.service_create_session(new_session_info)
            current_app.logger.info("Finishing API function login with result: " + str(new_session.session_id))
            session["session_id"] = new_session.session_id
            flash(message="Welcome!", category="success")
            return redirect(url_for("main_route.home"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function login with error: " + str(error))
            flash(message=str(error), category="error")
            return render_template("Customer/Login.html"), 400
    else:
        return render_template("Customer/Login.html")
