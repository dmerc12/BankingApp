import datetime
from flask_cors import CORS
from flask import Flask, request, jsonify
from PythonAPI.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.Entities.Transaction import Transaction
from PythonAPI.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from PythonAPI.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from PythonAPI.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

app: Flask = Flask(__name__)
CORS(app)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

banking_app: Flask = Flask(__name__)
CORS(banking_app)


@banking_app.route("/delete/account", methods=["DELETE"])
def delete_account():
    banking_app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    banking_app.logger.info("Beginning API function delete account")
    try:
        id_info: dict = request.get_json()
        session_id = int(id_info["sessionId"])
        account_id = id_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_delete_account(account_id)
        result_json = jsonify(result)
        banking_app.logger.info("Finishing API function delete account")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        banking_app.logger.error(f"Error with API function delete account with description: {str(error)}")
        return jsonify(message), 400

@banking_app.route("/get/all/transactions", methods=["PATCH"])
def get_all_transactions():
    banking_app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    banking_app.logger.info("Beginning API function get all transactions")
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
        banking_app.logger.info("Finishing API function get all transactions")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        banking_app.logger.error(f"{request.get_json()}, {request.path}, {datetime.datetime}")
        return jsonify(message), 400

banking_app.run()
