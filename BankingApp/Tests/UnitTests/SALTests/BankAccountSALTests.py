from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.Entities.BankAccount import BankAccount
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALImplementation import BankAccountSALImplementation

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

def test_service_create_account_success():
    result = account_sao.service_create_account(successful_account)
    assert result.account_id != 0

def test_service_get_account_by_id_account_not_found():
    try:
        account_sao.service_get_account_by_id("-50000")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_get_account_by_id_account_id_left_empty():
    try:
        account_sao.service_get_account_by_id("")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field cannot be left empty, please try again!"

def test_service_get_account_by_id_success():
    result = account_sao.service_get_account_by_id(str(successful_account.account_id))
    assert result is not None

def test_service_get_all_accounts_by_id_customer_id_left_empty():
    try:
        account_sao.service_get_all_accounts("")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field cannot be left empty, please try again!"

def test_service_get_all_accounts_by_id_none_found():
    try:
        account_sao.service_get_all_accounts("-2")
        assert False
    except FailedTransaction as error:
        assert str(error) == "No accounts found, please try again!"

def test_service_get_all_accounts_success():
    result = account_sao.service_get_all_accounts(str(successful_account.customer_id))
    assert len(result) >= 0

def test_service_deposit_amount_left_empty():
    try:
        account_sao.service_deposit(str(successful_account.account_id), "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit amount field cannot be left empty, please try again!"

def test_service_deposit_account_id_left_empty():
    try:
        account_sao.service_deposit("", "50.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit account ID field cannot be left empty, please try again!"

def test_service_deposit_account_not_found():
    try:
        account_sao.service_deposit("-5000000000", "50.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_deposit_amount_negative():
    try:
        account_sao.service_deposit(str(successful_account.account_id), "-25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit amount field cannot be negative or 0.00, please try again!"

def test_service_deposit_success():
    result = account_sao.service_deposit(str(successful_account.account_id), "25.00")
    assert result.balance == 75.00

def test_service_withdraw_amount_left_empty():
    try:
        account_sao.service_withdraw(str(successful_account.account_id), "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw amount field cannot be left empty, please try again!"

def test_service_withdraw_account_id_left_empty():
    try:
        account_sao.service_withdraw("", "50.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw account ID field cannot be left empty, please try again!"

def test_service_withdraw_account_not_found():
    try:
        account_sao.service_withdraw("-5000000000", "50.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_withdraw_amount_negative():
    try:
        account_sao.service_withdraw(str(successful_account.account_id), "-25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw amount field cannot be negative or 0.00, please try again!"

def test_service_withdraw_insufficient_funds():
    try:
        account_sao.service_withdraw(str(successful_account.account_id), "50000.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Insufficient funds, please try again!"

def test_service_withdraw_success():
    result = account_sao.service_withdraw(str(successful_account.account_id), "25.00")
    assert result.balance == 50.00

def test_service_transfer_withdraw_account_id_left_empty():
    try:
        account_sao.service_transfer("", "-1", "25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The withdraw account ID field cannot be left empty, please try again!"

def test_service_transfer_deposit_account_id_left_empty():
    try:
        account_sao.service_transfer(str(successful_account.account_id), "", "25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The deposit account ID field cannot be left empty, please try again!"

def test_service_transfer_amount_left_empty():
    try:
        account_sao.service_transfer(str(successful_account.account_id), "-1", "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transfer field cannot be left empty, please try again!"

def test_service_transfer_withdraw_account_id_not_found():
    try:
        account_sao.service_transfer("-5000000000", "-1", "25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_transfer_deposit_account_id_not_found():
    try:
        account_sao.service_transfer(str(successful_account.account_id), "-50000000000", "25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_transfer_amount_negative():
    try:
        account_sao.service_transfer(str(successful_account.account_id), "-1", "-25.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The transfer amount field cannot be negative or 0.00, please try again!"

def test_service_transfer_insufficient_funds():
    try:
        account_sao.service_transfer(str(successful_account.account_id), "-1", "500000.00")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Insufficient funds, please try again!"

def test_service_transfer_success():
    result = account_sao.service_transfer(str(successful_account.account_id), "-1", "50.00")
    assert result

def test_service_delete_account_left_empty():
    try:
        account_sao.service_delete_account("")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The account ID field cannot be left empty, please try again!"

def test_service_delete_account_not_found():
    try:
        account_sao.service_delete_account("-500000")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This account cannot be found, please try again!"

def test_service_delete_account_success():
    result = account_sao.service_delete_account(str(successful_account.account_id))
    assert result

def test_service_delete_all_accounts_customer_id_not_int():
    try:
        account_sao.service_delete_all_accounts("")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field cannot be left empty!, please try again!"

def test_service_delete_all_accounts_success():
    result = account_sao.service_delete_all_accounts("-2")
    assert result
