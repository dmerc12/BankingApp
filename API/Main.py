import datetime
import logging
import os.path
from flask_cors import CORS
from flask import Flask, request, jsonify
from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.BankAccount import BankAccount
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from Entities.Session import Session
from Entities.Transaction import Transaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

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


@app.before_request
def set_up_logs():
    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = "../Documentation/Logs/"
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)
    log_file = os.path.join("../Documentation/Logs/", 'BankingLogs.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)


@app.route("/login", methods=["POST"])
def login():
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
    )
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function login")
    try:
        login_credentials: dict = request.get_json()
        username = login_credentials["username"]
        password = login_credentials["password"]
        result = customer_sao.service_login(username, password)
        new_session_info = Session(0, result.customer_id, str(datetime.datetime.now()),
                                   str(datetime.datetime.now() + datetime.timedelta(0, 0, 0, 0, 0, 1)))
        new_session = session_sao.service_create_session(new_session_info)
        # use to send session ID to be stored in session storage, will change here when implementing cookies
        result_dictionary = {
            "sessionId": new_session.session_id
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function login")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function login with description: {str(error)}")
        return jsonify(message), 400


@app.route("/logout", methods=["DELETE"])
def delete_session():
    app.logger.info("Beginning API function delete session")
    try:
        session_info: dict = request.get_json()
        session_id = int(session_info["sessionId"])
        result = session_sao.service_delete_session(session_id)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function delete session")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function create customer with description: {str(error)}")
        return jsonify(message), 400


@app.route("/create/customer", methods=["POST"])
def create_customer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function create customer")
    try:
        customer_info: dict = request.get_json()
        new_customer = Customer(0, customer_info["firstName"], customer_info["lastName"], customer_info["username"],
                                customer_info["password"], customer_info["email"], customer_info["phoneNumber"],
                                customer_info["address"])
        result = customer_sao.service_create_customer(new_customer)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function create customer")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function create customer with description: {str(error)}")
        return jsonify(message), 400


@app.route("/update/customer", methods=["PATCH"])
def update_customer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function update customer")
    try:
        new_customer_information: dict = request.get_json()
        session_id = int(new_customer_information["sessionId"])
        current_customer_id = session_sao.service_get_session(session_id).customer_id
        updated_customer_information = Customer(current_customer_id,
                                                new_customer_information["firstName"],
                                                new_customer_information["lastName"],
                                                new_customer_information["username"],
                                                new_customer_information["password"],
                                                new_customer_information["email"],
                                                new_customer_information["phoneNumber"],
                                                new_customer_information["address"])
        result = customer_sao.service_update_customer(updated_customer_information)
        result_dictionary = {
            "firstName": result.first_name,
            "lastName": result.last_name,
            "username": result.username,
            "password": result.password,
            "email": result.email,
            "phoneNumber": result.phone_number,
            "address": result.address
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function update customer")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function update customer with description: {str(error)}")
        return jsonify(message), 400


@app.route("/delete/customer", methods=["DELETE"])
def delete_customer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function delete customer")
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
        app.logger.info("Finishing API function delete customer")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function delete customer with description: {str(error)}")
        return jsonify(message), 400


@app.route("/create/account", methods=["POST"])
def create_account():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function create account")
    try:
        account_data: dict = request.get_json()
        session_id = int(account_data["sessionId"])
        balance = float(account_data["balance"])
        customer_id = session_sao.service_get_session(session_id).customer_id
        new_account: BankAccount = BankAccount(0, customer_id,
                                               balance)
        result = account_sao.service_create_account(new_account)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = result.account_id
        transaction_amount = result.balance
        setup_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", transaction_account_id,
                                        transaction_amount)
        transaction_sao.service_create_transaction(setup_transaction)
        app.logger.info("Finishing API function create account")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function create account with description: {str(error)}")
        return jsonify(message), 400


@app.route("/get/all/accounts", methods=["PATCH"])
def get_all_accounts():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get all accounts")
    try:
        requested_info: dict = request.get_json()
        session_id = int(requested_info["sessionId"])
        customer_id = str(session_sao.service_get_session(session_id).customer_id)
        result = account_sao.service_get_all_accounts(customer_id)
        result_dictionary = {
            "accountList": result
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function get all accounts")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message":  str(error)
        }
        app.logger.error(f"Error with API function get all accounts with description: {str(error)}")
        return jsonify(message), 400


@app.route("/deposit", methods=["PATCH"])
def deposit():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function deposit")
    try:
        deposit_info: dict = request.get_json()
        session_id = int(deposit_info["sessionId"])
        deposit_amount = deposit_info["depositAmount"]
        account_id = deposit_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_deposit(account_id, deposit_amount)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = deposit_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", int(transaction_account_id),
                                          float(transaction_amount))
        transaction_sao.service_create_transaction(deposit_transaction)
        app.logger.info("Finishing API function deposit")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function deposit with description: {str(error)}")
        return jsonify(message), 400

@app.route("/withdraw", methods=["PATCH"])
def withdraw():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function withdraw")
    try:
        withdraw_info: dict = request.get_json()
        session_id = int(withdraw_info["sessionId"])
        withdraw_amount = withdraw_info["withdrawAmount"]
        account_id = withdraw_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_withdraw(account_id, withdraw_amount)
        result_dictionary = {
            "accountId": result.account_id,
            "balance": result.balance
        }
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = withdraw_amount
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw", int(transaction_account_id),
                                           float(transaction_amount))
        transaction_sao.service_create_transaction(withdraw_transaction)
        app.logger.info("Finishing API function withdraw")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function withdraw with description: {str(error)}")
        return jsonify(message), 400

@app.route("/transfer", methods=["PATCH"])
def transfer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function transfer")
    try:
        transfer_info: dict = request.get_json()
        session_id = int(transfer_info["sessionId"])
        session_sao.service_get_session(session_id)
        transfer_amount = transfer_info["transferAmount"]
        withdraw_account_id = transfer_info["withdrawAccountId"]
        deposit_account_id = transfer_info["depositAccountId"]
        result = account_sao.service_transfer(withdraw_account_id, deposit_account_id, transfer_amount)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        withdraw_transaction_account_id = withdraw_account_id
        withdraw_transaction_amount = transfer_amount
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw",
                                           int(withdraw_transaction_account_id), float(withdraw_transaction_amount))
        transaction_sao.service_create_transaction(withdraw_transaction)
        deposit_transaction_account_id = deposit_account_id
        deposit_transaction_amount = transfer_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit",
                                          int(deposit_transaction_account_id), float(deposit_transaction_amount))
        transaction_sao.service_create_transaction(deposit_transaction)
        app.logger.info("Finishing API function transfer")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function transfer with description: {str(error)}")
        return jsonify(message), 400

@app.route("/delete/account", methods=["DELETE"])
def delete_account():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function delete account")
    try:
        id_info: dict = request.get_json()
        session_id = int(id_info["sessionId"])
        account_id = id_info["accountId"]
        session_sao.service_get_session(session_id)
        result = account_sao.service_delete_account(account_id)
        result_json = jsonify(result)
        app.logger.info("Finishing API function delete account")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function delete account with description: {str(error)}")
        return jsonify(message), 400

@app.route("/get/all/transactions", methods=["PATCH"])
def get_all_transactions():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get all transactions")
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
        app.logger.info("Finishing API function get all transactions")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"{request.get_json()}, {request.path}, {datetime.datetime}")
        return jsonify(message), 400

app.run()
