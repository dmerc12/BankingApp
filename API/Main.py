import datetime
import logging
import os.path

from flask import Flask, request, jsonify
from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.BankAccount import BankAccount
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from Entities.Transaction import Transaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

app: Flask = Flask(__name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)
transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

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
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function login")
    try:
        login_credentials: dict = request.get_json()
        username = login_credentials["username"]
        password = login_credentials["password"]
        result = customer_sao.service_login(username, password)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function login")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function login with description: {str(error)}")
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

@app.route("/get/customer", methods=["GET"])
def get_customer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get customer")
    try:
        requested_id: dict = request.get_json()
        customer_id = requested_id["customerId"]
        result = customer_sao.service_get_customer_by_id(customer_id)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function get customer")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function get customer with description: {str(error)}")
        return jsonify(message), 400

@app.route("/update/customer", methods=["PATCH"])
def update_customer():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function update customer")
    try:
        new_customer_information: dict = request.get_json()
        updated_customer_information = Customer(new_customer_information["customerId"],
                                                new_customer_information["firstName"],
                                                new_customer_information["lastName"],
                                                new_customer_information["username"],
                                                new_customer_information["password"],
                                                new_customer_information["email"],
                                                new_customer_information["phoneNumber"],
                                                new_customer_information["address"])
        result = customer_sao.service_update_customer(updated_customer_information)
        result_dictionary = result.convert_to_dictionary()
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
        requested_id = requested_info["customerId"]
        result = customer_sao.service_delete_customer(requested_id)
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
        new_account: BankAccount = BankAccount(account_data["accountId"], account_data["customerId"],
                                               account_data["balance"])
        result = account_sao.service_create_account(new_account)
        result_dictionary = result.convert_to_dictionary()
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

@app.route("/get/account", methods=["GET"])
def get_account():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get account")
    try:
        account_information: dict = request.get_json()
        retrieved_id = account_information["accountId"]
        result = account_sao.service_get_account_by_id(retrieved_id)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function get account")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function get account with description: {str(error)}")
        return jsonify(message), 400

@app.route("/get/all/accounts", methods=["GET"])
def get_all_accounts():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get all accounts")
    try:
        requested_info: dict = request.get_json()
        customer_id = requested_info["customerId"]
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
        deposit_amount = deposit_info["depositAmount"]
        account_id = deposit_info["accountId"]
        result = account_sao.service_deposit(account_id, deposit_amount)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = deposit_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", transaction_account_id,
                                          transaction_amount)
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
        withdraw_amount = withdraw_info["withdrawAmount"]
        account_id = withdraw_info["accountId"]
        result = account_sao.service_withdraw(account_id, withdraw_amount)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        transaction_account_id = account_id
        transaction_amount = withdraw_amount
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw", transaction_account_id,
                                           transaction_amount)
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
        withdraw_transaction = Transaction(0, str(datetime.datetime.now()), "withdraw", withdraw_transaction_account_id,
                                           withdraw_transaction_amount)
        transaction_sao.service_create_transaction(withdraw_transaction)
        deposit_transaction_account_id = deposit_account_id
        deposit_transaction_amount = transfer_amount
        deposit_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", deposit_transaction_account_id,
                                          deposit_transaction_amount)
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
        account_id = id_info["accountId"]
        transaction_sao.service_delete_all_transactions(account_id)
        result = account_sao.service_delete_account(account_id)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function delete account")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"Error with API function delete account with description: {str(error)}")
        return jsonify(message), 400

@app.route("/get/transaction", methods=["GET"])
def get_transaction_by_id():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get transaction by ID")
    try:
        id_info: dict = request.get_json()
        transaction_id = id_info["transactionId"]
        result = transaction_sao.service_get_transaction_by_id(transaction_id)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function get transaction by ID")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"{request.get_json()}, {request.path}, {datetime.datetime}")
        return jsonify(message), 400

@app.route("/get/all/transactions", methods=["GET"])
def get_all_transactions():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get all transactions")
    try:
        id_info: dict = request.get_json()
        account_id = id_info["accountId"]
        result = transaction_sao.service_get_all_transactions(account_id)
        result_dictionary = {
            "result": result
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

@app.route("/delete/transaction", methods=["DELETE"])
def delete_transaction():
    app.logger.info(f"{request.get_json()}, {request}, {request.path}, {datetime.datetime.now()}")
    app.logger.info("Beginning API function get delete transaction")
    try:
        id_info: dict = request.get_json()
        transaction_id = id_info["transactionId"]
        result = transaction_sao.service_delete_transaction(transaction_id)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        app.logger.info("Finishing API function delete transaction")
        return result_json, 201
    except FailedTransaction as error:
        message = {
            "message": str(error)
        }
        app.logger.error(f"{request.get_json()}, {request.path}, {datetime.datetime}")
        return jsonify(message), 400

app.run()
