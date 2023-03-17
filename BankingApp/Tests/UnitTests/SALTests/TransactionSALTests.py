from datetime import datetime

from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

successful_transaction = Transaction(0, str(datetime.now()), "deposit", -1, 50.00)

def test_service_create_transaction_datetime_not_string():
    try:
        test_transaction = Transaction(0, 1, "deposit", 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The date and time field must be a string, please try again!"

def test_service_create_transaction_datetime_too_long():
    try:
        test_transaction = Transaction(0, "this is way too long and so it should fail", "deposit", 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The date and time field cannot exceed 26 characters, please try again!"

def test_service_create_transaction_datetime_empty():
    try:
        test_transaction = Transaction(0, "", "deposit", 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The date and time field cannot be left empty, please try again!"

def test_service_create_transaction_type_not_string():
    try:
        test_transaction = Transaction(0, str(datetime.now()), 1, 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction type field must be a string, please try again!"

def test_service_create_transaction_type_too_long():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "this is way too long and so it should fail", 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction type field cannot exceed 8 characters, please try again!"

def test_service_create_transaction_type_empty():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "", 1, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction type field cannot be left empty, please try again!"

def test_service_create_transaction_account_id_not_integer():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "deposit", "1", 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field must be an integer, please try again!"

def test_service_create_transaction_account_id_not_found():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "deposit", -5000000, 25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_create_transaction_amount_not_float():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "deposit", 1, "25.00")
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction amount field must be a float, please try again!"

def test_service_create_transaction_amount_negative():
    try:
        test_transaction = Transaction(0, str(datetime.now()), "deposit", 1, -25.00)
        transaction_sao.service_create_transaction(test_transaction)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction amount field cannot be negative, please try again!"

def test_service_create_transaction_success():
    result = transaction_sao.service_create_transaction(successful_transaction)
    assert result.transaction_id != 0

def test_service_get_transaction_by_id_not_integer():
    try:
        transaction_sao.service_get_transaction_by_id("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction ID field must be an integer, please try again!"

def test_service_get_transaction_by_id_not_found():
    try:
        transaction_sao.service_get_transaction_by_id(-50000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This transaction cannot be found, please try again!"

def test_service_get_transaction_by_id_success():
    result = transaction_sao.service_get_transaction_by_id(successful_transaction.transaction_id)
    assert result is not None

def test_service_get_all_transactions_account_id_not_integer():
    try:
        transaction_sao.service_get_all_transactions("this won't work")
    except FailedTransaction as error:
        assert str(error) == "The account ID field must be an integer, please try again!"

def test_service_get_all_transactions_none_found():
    try:
        transaction_sao.service_get_all_transactions(-50000000)
    except FailedTransaction as error:
        assert str(error) == "No transactions found, please try again!"

def test_service_get_all_transactions_success():
    result = transaction_sao.service_get_all_transactions(successful_transaction.account_id)
    assert len(result) > 0

def test_delete_transaction_id_not_integer():
    try:
        transaction_sao.service_delete_transaction("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transaction ID field must be an integer, please try again!"

def test_delete_transaction_not_found():
    try:
        transaction_sao.service_delete_transaction(-5000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This transaction cannot be found, please try again!"

def test_service_delete_transaction_success():
    result = transaction_sao.service_delete_transaction(successful_transaction.transaction_id)
    assert result

def test_service_delete_all_transactions_account_id_not_integer():
    try:
        transaction_sao.service_delete_all_transactions("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field musts be an integer, please try again!"

def test_service_delete_all_transactions_success():
    result = transaction_sao.service_delete_all_transactions(successful_transaction.account_id)
    assert result
