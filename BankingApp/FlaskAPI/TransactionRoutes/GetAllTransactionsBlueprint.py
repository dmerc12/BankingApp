from flask import Blueprint, jsonify, request, current_app

from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

get_relevant_transactions = Blueprint('get_relevant_transactions', __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

@get_relevant_transactions.route("/get/all/transactions", methods=["PATCH"])
def get_all_transactions():
    try:
        id_info: dict = request.get_json()
        current_app.logger.info("Beginning API function get all transactions with data: " + str(id_info))
        session_id = int(id_info["sessionId"])
        account_id = int(id_info["accountId"])
        session_sao.service_get_session(session_id)
        result = transaction_sao.service_get_all_transactions(account_id)
        result_dictionary = {
            "transactionList": result
        }
        result_json = jsonify(result_dictionary)
        current_app.logger.info("Finishing API function get all transactions with resulting information: "
                                + str(result_json))
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        current_app.logger.error("Error with API function get all transactions with message: " + str(error))
        return jsonify(message), 400
