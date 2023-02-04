from flask import Blueprint, request, jsonify

from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

logout = Blueprint('logout', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@logout.route("/logout", methods=["DELETE"])
def logout():
    try:
        session_info: dict = request.get_json()
        session_id = int(session_info["sessionId"])
        result = session_sao.service_delete_session(session_id)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
