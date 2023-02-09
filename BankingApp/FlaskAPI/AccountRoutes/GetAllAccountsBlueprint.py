from flask import jsonify, request, Blueprint

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

get_relevant_accounts = Blueprint('get_relevant_accounts', __name__)

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_relevant_accounts.route("/get/all/accounts", methods=["PATCH"])
def get_all_accounts():
    try:
        requested_info: dict = request.get_json()
        session_id = int(requested_info["sessionId"])
        customer_id = str(session_sao.service_get_session(session_id).customer_id)
        result = account_sao.service_get_all_accounts(customer_id)
        result_dictionary = {
            "accountList": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message":  str(error)
        }
        return jsonify(message), 400
