from datetime import datetime
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from Entities.Transaction import Transaction
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation

transaction_dao = TransactionDALImplementation()
transaction_sao = TransactionSALImplementation(transaction_dao)

successful_transaction = Transaction(0, str(datetime.now()), "deposit", -1, 50.00)

def test_service_create_transaction_datetime_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_datetime_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_type_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_type_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_account_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_account_id_not_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_amount_not_float():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_amount_negative():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_transaction_success():
    result = transaction_sao.service_create_transaction(successful_transaction)
    assert result.transaction_id != 0

def test_service_get_transaction_by_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_transaction_by_id_not_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_transaction_by_id_success():
    result = transaction_sao.service_get_transaction_by_id(successful_transaction.transaction_id)
    assert result is not None

def test_service_get_all_transactions_account_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_all_transactions_none_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_all_transactions_success():
    result = transaction_sao.service_get_all_transactions(successful_transaction.account_id)
    assert len(result) >= 0

def test_delete_transaction_transaction_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_delete_transaction_not_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_delete_transaction_success():
    result = transaction_sao.service_delete_transaction(successful_transaction.transaction_id)
    assert result
