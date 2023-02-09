from flask import Blueprint, jsonify, request

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

load_customer_info = Blueprint('load_customer_info', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@load_customer_info.route("/load/customer/info", methods=["PATCH"])
def get_customer_info():
    try:
        session_info: dict = request.get_json()
        session_id = int(session_info["sessionId"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        result = customer_sao.service_get_customer_by_id(customer_id)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
