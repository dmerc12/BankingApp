from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from Entities.BankAccount import BankAccount

account_dao = BankAccountDALImplementation()
test_account = BankAccount(0, -1, 50.00)

def test_create_account_success():
    result = account_dao.create_account(test_account)
    assert result.account_id != 0

def test_get_account_by_id_success():
    result = account_dao.get_account_by_id(test_account.account_id)
    assert result.account_id == test_account.account_id

def test_get_all_accounts_success():
    result = account_dao.get_all_accounts(test_account.customer_id)
    assert len(result) > 0

def test_get_accounts_for_delete_success():
    result = account_dao.get_accounts_for_delete(-2)
    assert len(result) > 0

def test_deposit_success():
    result = account_dao.deposit(test_account.account_id, 25.00)
    assert result.balance == 75.00

def test_withdraw_success():
    result = account_dao.withdraw(test_account.account_id, 25.00)
    assert result.balance == 50.00

def test_transfer_success():
    result = account_dao.transfer(test_account.account_id, -1, 25.00)
    assert result

def test_delete_account_success():
    result = account_dao.delete_account(test_account.account_id)
    assert result

def test_delete_all_accounts_success():
    result = account_dao.delete_all_accounts(-4)
    assert result
