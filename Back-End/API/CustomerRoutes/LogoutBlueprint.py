from flask import Blueprint, jsonify, current_app

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

logout_route = Blueprint('logout_route', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@logout_route.route("/api/logout/<int:session_id>", methods=["DELETE"])
def logout(session_id):
    try:
        current_app.logger.info("Beginning API function logout with data: " + str(session_id))
        result = session_sao.service_delete_session(session_id)
        current_app.logger.info("Finishing API function logout with result: " + str(result))
        response = {
            "message": "Goodbye!"
        }
        return jsonify(response), 200
    except FailedTransaction as error:
        current_app.logger.error("Error with API function logout with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
