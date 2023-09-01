from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta

from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

change_password_route = Blueprint("change_password_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@change_password_route.route("/change/password/now", methods=["PUT"])
def change_password_api():
    try:
        session_id = request.json.get("sessionId")
        new_password = request.json.get("password")
        confirmation_password = request.json.get("confirmationPassword")
        session = session_sao.service_get_session(session_id)
        customer_id = session.customer_id
        current_app.logger.info("Beginning API function change password with data: " + str(request.json))
        customer_sao.service_change_password(customer_id, new_password, confirmation_password)
        new_expire_date_time = datetime.now() + timedelta(minutes=15)
        session.expire_date_time = new_expire_date_time
        session_dao.update_session(session)
        current_app.logger.info("Finishing API function change password")
        response = {
            "message": "Password successfully updated!"
        }
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function change password with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
