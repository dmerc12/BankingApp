from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from Entities.BankAccount import BankAccount
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation

account_dao = BankAccountDALImplementation()
account_sao = BankAccountSALImplementation(account_dao)

successful_account = BankAccount(0, -1, 50.00)

def test_service_create_account_balance_negative():
    try:
        test_account = BankAccount(successful_account.account_id, successful_account.customer_id, -25.00)
        account_sao.service_create_account(test_account)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The balance field cannot be negative, please try again!"

def test_service_create_account_no_customer_found():
    try:
        test_account = BankAccount(successful_account.account_id, -500000000, 25.00)
        account_sao.service_create_account(test_account)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_create_account_amount_zero():
    try:
        test_account = BankAccount(successful_account.account_id, successful_account.customer_id, 0.00)
        account_sao.service_create_account(test_account)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The balance field must be greater than 0.00, please try again!"

def test_service_create_account_success():
    result = account_sao.service_create_account(successful_account)
    assert result.account_id != 0

def test_service_get_account_by_id_account_not_found():
    try:
        account_sao.service_get_account_by_id(-50000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_get_account_by_id_account_id_not_integer():
    try:
        account_sao.service_get_account_by_id("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field must be an integer, please try again!"

def test_service_get_account_by_id_success():
    result = account_sao.service_get_account_by_id(successful_account.account_id)
    assert result is not None

def test_service_get_all_accounts_by_id_customer_id_not_integer():
    try:
        account_sao.service_get_all_accounts("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field must be an integer, please try again!"

def test_service_get_all_accounts_by_id_none_found():
    try:
        account_sao.service_get_all_accounts(-3000000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "No accounts found, please try again!"

def test_service_get_all_accounts_success():
    result = account_sao.service_get_all_accounts(successful_account.customer_id)
    assert len(result) > 0

def test_service_deposit_account_id_left_not_integer():
    try:
        account_sao.service_deposit("this won't work", 50.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit account ID field must be an integer, please try again!"

def test_service_deposit_account_not_found():
    try:
        account_sao.service_deposit(-5000000000, 50.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_deposit_amount_negative():
    try:
        account_sao.service_deposit(successful_account.account_id, -25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit amount field cannot be negative or 0.00, please try again!"

def test_service_deposit_success():
    result = account_sao.service_deposit(successful_account.account_id, 25.00)
    assert result.balance == 75.00

def test_service_withdraw_account_id_not_integer():
    try:
        account_sao.service_withdraw("this won't work", 50.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw account ID field must be an integer, please try again!"

def test_service_withdraw_account_not_found():
    try:
        account_sao.service_withdraw(-5000000000, 50.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_withdraw_amount_negative():
    try:
        account_sao.service_withdraw(successful_account.account_id, -25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw amount field cannot be negative or 0.00, please try again!"

def test_service_withdraw_insufficient_funds():
    try:
        account_sao.service_withdraw(successful_account.account_id, 50000.0)
        assert False
    except FailedTransaction as error:
        assert str(error) == "Insufficient funds, please try again!"

def test_service_withdraw_success():
    result = account_sao.service_withdraw(successful_account.account_id, 25.00)
    assert result.balance == 50.00

def test_service_transfer_withdraw_account_id_not_integer():
    try:
        account_sao.service_transfer("this won't work", -1, 25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw account ID field must be an integer, please try again!"

def test_service_transfer_deposit_account_id_not_integer():
    try:
        account_sao.service_transfer(successful_account.account_id, "this won't work", 25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit account ID field must be an integer, please try again!"

def test_service_transfer_withdraw_account_id_not_found():
    try:
        account_sao.service_transfer(-5000000000, -1, 25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_transfer_deposit_account_id_not_found():
    try:
        account_sao.service_transfer(successful_account.account_id, -50000000000, 25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_transfer_account_ids_same():
    try:
        account_sao.service_transfer(successful_account.account_id, successful_account.account_id, 25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit and withdraw accounts cannot be the same, please try again!"

def test_service_transfer_amount_negative():
    try:
        account_sao.service_transfer(successful_account.account_id, -1, -25.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transfer amount field cannot be negative or 0.00, please try again!"

def test_service_transfer_insufficient_funds():
    try:
        account_sao.service_transfer(successful_account.account_id, -1, 500000.00)
        assert False
    except FailedTransaction as error:
        assert str(error) == "Insufficient funds, please try again!"

def test_service_transfer_success():
    result = account_sao.service_transfer(successful_account.account_id, -1, 50.00)
    assert result

def test_service_delete_account_not_integer():
    try:
        account_sao.service_delete_account("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field must be an integer, please try again!"

def test_service_delete_account_not_found():
    try:
        account_sao.service_delete_account(-500000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_delete_account_success():
    result = account_sao.service_delete_account(successful_account.account_id)
    assert result

def test_service_delete_all_accounts_customer_id_not_integer():
    try:
        account_sao.service_delete_all_accounts("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field must be an integer, please try again!"

def test_service_delete_all_accounts_success():
    result = account_sao.service_delete_all_accounts(-2)
    assert result
