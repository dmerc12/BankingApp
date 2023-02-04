from flask import Blueprint, jsonify, request

from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from PythonAPI.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

get_all_transactions = Blueprint('get_all_transactions', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@get_all_transactions.route("/get/all/transactions", methods=["PATCH"])
def get_all_transactions():
    try:
        id_info: dict = request.get_json()
        session_id = int(id_info["sessionId"])
        account_id = int(id_info["accountId"])
        session_sao.service_get_session(session_id)
        result = transaction_sao.service_get_all_transactions(account_id)
        result_dictionary = {
            "transactionList": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        return jsonify(message), 400
