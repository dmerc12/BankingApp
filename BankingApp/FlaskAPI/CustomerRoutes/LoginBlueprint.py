import datetime

from flask import Blueprint, request, jsonify, current_app

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

new_login = Blueprint('new_login', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@new_login.route("/login", methods=["POST"])
def login():
    try:
        login_credentials: dict = request.get_json()
        current_app.logger.info("Beginning API function login with data: " + str(login_credentials))
        email = login_credentials["email"]
        password = login_credentials["password"]
        result = customer_sao.service_login(email, password)
        new_session_info = Session(0, result.customer_id, str(datetime.datetime.now()),
                                   str(datetime.datetime.now() + datetime.timedelta(0, 0, 0, 0, 0, 1)))
        new_session = session_sao.service_create_session(new_session_info)
        # use to send session ID to be stored in session storage, will change here when implementing cookies
        result_dictionary = {
            "sessionId": new_session.session_id
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function login with result: " + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function login with error: " + str(error))
        return jsonify(message), 400
