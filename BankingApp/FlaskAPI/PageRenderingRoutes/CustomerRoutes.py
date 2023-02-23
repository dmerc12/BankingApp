import datetime

from flask import Blueprint, render_template, request, jsonify, current_app, make_response, redirect

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

customer_routes = Blueprint("customer_routes", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@customer_routes.route("/", methods=["GET"])
@customer_routes.route("/login", methods=["GET"])
def login():
    return render_template("Customer/Login.html")

@customer_routes.route("/home", methods=["GET"])
def home():
    return render_template("Main/Home.html")

@customer_routes.route("/manage/customer", methods=["GET"])
def manage_customer():
    return render_template("Customer/ManageCustomer.html")

@customer_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login_form = request.form
        email = login_form["email"]
        password = login_form["password"]
        current_app.logger.info("Beginning API function login with data: " + str(email) + ", " + str(password))

        result = customer_sao.service_login(email, password)
        new_session_info = Session(0, result.customer_id, str(datetime.datetime.now()),
                                   str(datetime.datetime.now() + datetime.timedelta(0, 0, 0, 0, 0, 1)))
        new_session = session_sao.service_create_session(new_session_info)
        result_dictionary = {
            "sessionId": new_session.session_id
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function login with result: " + str(result_json))
        login_response = make_response(result_json, 201)
        return login_response, redirect(home.url)
    else:
        return render_template("Customer/Register.html")
