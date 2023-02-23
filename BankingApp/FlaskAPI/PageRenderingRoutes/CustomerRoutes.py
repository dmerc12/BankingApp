import datetime

from flask import Blueprint, render_template, request, jsonify, current_app, make_response, redirect, url_for, flash

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

customer_routes = Blueprint("customer_routes", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@customer_routes.route("/", methods=["GET", "POST"])
@customer_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]
            current_app.logger.info("Beginning API function login with data: " + str(email) + ", " + str(password))

            result = customer_sao.service_login(email, password)
            new_session_info = Session(0, result.customer_id, str(datetime.datetime.now()),
                                       str(datetime.datetime.now() + datetime.timedelta(0, 0, 0, 0, 0, 1)))
            new_session = session_sao.service_create_session(new_session_info)
            current_app.logger.info("Finishing API function login with result: " + str(new_session))
            login_response = make_response()
            login_response.status_code = 201
            login_response.set_cookie('session_id', str(new_session.session_id))
            return redirect(url_for("customer_routes.home"))
        except FailedTransaction as error:
            current_app.logger.error("Error with API function login with error: " + str(error))
            flash(str(error))
            return render_template("Customer/Login.html"), 400
    else:
        return render_template("Customer/Login.html")

@customer_routes.route("/home", methods=["GET"])
def home():
    session_id = request.cookies.get("session_id")
    return render_template("Main/Home.html")

@customer_routes.route("/manage/customer", methods=["GET"])
def manage_customer():
    return render_template("Customer/ManageCustomer.html")

@customer_routes.route("/register", methods=["GET", "POST"])
def register():
    return render_template("Customer/Register.html")
