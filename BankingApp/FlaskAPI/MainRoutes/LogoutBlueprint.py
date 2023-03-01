from flask import Blueprint, jsonify, current_app, session, redirect, url_for

from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

new_logout = Blueprint('new_logout', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@new_logout.route("/logout", methods=["GET", "DELETE"])
def logout():
    try:
        session_id = session["session_id"]
        current_app.logger.info("Beginning API function logout with data: " + str(session_id))
        result = session_sao.service_delete_session(session_id)
        session.clear()
        current_app.logger.info("Finishing API function logout with result: " + str(result))
        return redirect(url_for("login_route.login"))
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function logout with error: " + str(error))
        return jsonify(message), 400
