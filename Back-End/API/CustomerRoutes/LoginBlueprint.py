import datetime

from flask import Blueprint, jsonify, request, current_app

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from Entities.Session import Session
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

login_route = Blueprint("login_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@login_route.route("/login-now", methods=["POST"])
def login():
    try:
        email = request.json.get("email")
        password = request.json.get("password")
        current_app.logger.info("Beginning API function login with data: " + str(email) + ", " + str(password))

        result = customer_sao.service_login(email, password)
        new_session_info = Session(0, result.customer_id, str(datetime.datetime.now() +
                                                              datetime.timedelta(minutes=15)))
        new_session = session_sao.service_create_session(new_session_info)
        current_app.logger.info("Finishing API function login with result: " + str(new_session.session_id))
        response = {
            "message": "Welcome!",
            "sessionId": new_session.session_id
        }
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function login with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400

