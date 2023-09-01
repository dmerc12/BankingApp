import datetime

from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.Transaction import Transaction

transaction_dao = TransactionDALImplementation()
test_transaction = Transaction(0, str(datetime.datetime.now()), "deposit", -1, 50.00)

def test_create_transaction_success():
    result = transaction_dao.create_transaction(test_transaction)
    assert result.transaction_id != 0

def test_get_transaction_success():
    result = transaction_dao.get_transaction_by_id(test_transaction.transaction_id)
    assert result is not None

def test_get_all_transactions_success():
    result = transaction_dao.get_all_transactions(test_transaction.account_id)
    assert len(result) >= 0

def test_delete_transaction_success():
    result = transaction_dao.delete_transaction(test_transaction.transaction_id)
    assert result

def test_delete_all_transactions_success():
    result = transaction_dao.delete_all_transactions(test_transaction.account_id)
    assert result
