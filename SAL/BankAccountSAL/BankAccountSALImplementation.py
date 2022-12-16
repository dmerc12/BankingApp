import logging
from typing import List
from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from Entities.BankAccount import BankAccount
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALInterface import BankAccountSALInterface

class BankAccountSALImplementation(BankAccountSALInterface):

    def __init__(self, account_dao: BankAccountDALImplementation):
        self.account_dao = account_dao

    def service_create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning SAL method create account")
        if type(account.customer_id) != int:
            logging.warning("SAL method create account, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        elif type(account.balance) != float:
            logging.warning("SAL method create account, balance not a float")
            raise FailedTransaction("The balance field must be a float, please try again!")
        elif account.balance < 0.00:
            logging.warning("SAL method create account, negative balance attempted")
            raise FailedTransaction("The balance field cannot be negative, please try again!")
        else:
            new_account = self.account_dao.create_account(account)
            logging.info("Finishing SAL method create account")
            return new_account

    def service_get_account_by_id(self, account_id: int) -> BankAccount:
        logging.info("Beginning SAL method get account by ID")
        if type(account_id) != int:
            logging.warning("SAL method get account by ID, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        else:
            account = self.account_dao.get_account_by_id(account_id)
            logging.info("Finishing SAL method get account by ID")
            return account

    def service_get_all_accounts(self, customer_id: int) -> List[str]:
        logging.info("Beginning SAL method get all accounts")
        if type(customer_id) != int:
            logging.warning("SAL method get all accounts, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            account_list = self.account_dao.get_all_accounts(customer_id)
            logging.info("Finishing SAL method get all accounts")
            return account_list

    def service_deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        logging.info("Beginning SAL method deposit")
        if type(account_id) != int:
            logging.warning("SAL method deposit, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        elif type(deposit_amount) != float:
            logging.warning("SAL method deposit, deposit amount not a float")
            raise FailedTransaction("The deposit amount field must be a float, please try again!")
        elif deposit_amount <= 0.00:
            logging.warning("SAL method deposit, deposit amount negative")
            raise FailedTransaction("The deposit amount field cannot be negative, please try again!")
        else:
            deposit_result = self.account_dao.deposit(account_id, deposit_amount)
            logging.info("Finishing SAL method deposit")
            return deposit_result

    def service_withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        logging.info("Beginning SAL method withdraw")
        if type(account_id) != int:
            logging.warning("SAL method withdraw, account ID not an integer")
            raise FailedTransaction("The account ID field is must be an integer, please try again!")
        elif type(withdraw_amount) != float:
            logging.warning("SAL method withdraw, withdraw amount not a float")
            raise FailedTransaction("The withdraw amount field must be a float, please try again!")
        elif withdraw_amount <= 0.00:
            logging.warning("SAL method withdraw, withdraw amount negative")
            raise FailedTransaction("The withdraw amount field cannot be negative, please try again!")
        else:
            updated_account_info = self.account_dao.deposit(account_id, withdraw_amount)
            logging.info("Finishing SAL method withdraw")
            return updated_account_info

    def service_transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        logging.info("Beginning SAL method transfer")
        if type(withdraw_account_id) != int:
            logging.warning("SAL method transfer, withdraw account ID not an integer")
            raise FailedTransaction("The withdraw account ID field must be an integer, please try again!")
        elif type(deposit_account_id) != int:
            logging.warning("SAL method transfer, deposit account ID not an integer")
            raise FailedTransaction("The deposit account ID field must be an integer, please try again!")
        elif type(transfer_amount) != float:
            logging.warning("SAL method transfer, transfer amount not a float")
            raise FailedTransaction("The transfer amount field must be a float, please try again!")
        elif transfer_amount <= 0.00:
            logging.warning("SAL method transfer, transfer amount negative")
            raise FailedTransaction("The transfer amount field cannot be negative, please try again!")
        else:
            current_withdraw_account_info = self.account_dao.get_account_by_id(withdraw_account_id)
            if (current_withdraw_account_info.balance - transfer_amount) < 0.00:
                logging.warning("SAL method transfer, insufficient funds")
                raise FailedTransaction("Insufficient funds, please try again!")
            else:
                result = self.account_dao.transfer(withdraw_account_id, deposit_account_id, transfer_amount)
                logging.info("Finishing SAL method transfer")
                return result

    def service_delete_account(self, account_id: int) -> bool:
        logging.info("Beginning SAL method delete account")
        if type(account_id) != int:
            logging.warning("SAL method delete account, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        else:
            result = self.account_dao.delete_account(account_id)
            if result is False:
                logging.warning("SAL method delete account, no account found to delete")
                raise FailedTransaction("No account found to delete, please try again!")
            else:
                logging.info("Finishing SAL method delete account")
                return result
