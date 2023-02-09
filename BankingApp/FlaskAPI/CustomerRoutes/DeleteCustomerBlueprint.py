from flask import Blueprint, jsonify, request

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

delete_this_customer = Blueprint('delete_this_customer', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_this_customer.route("/delete/customer", methods=["DELETE"])
def delete_customer():
    try:
        requested_info = request.get_json()
        session_id = int(requested_info["sessionId"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        session_sao.service_delete_all_sessions(customer_id)
        result = customer_sao.service_delete_customer(customer_id)
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
