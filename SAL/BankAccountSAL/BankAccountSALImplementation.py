import logging
from typing import List
from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from Entities.BankAccount import BankAccount
from SAL.BankAccountSAL.BankAccountSALInterface import BankAccountSALInterface

class BankAccountSALImplementation(BankAccountSALInterface):

    def __init__(self, account_dao: BankAccountDALImplementation):
        self.account_dao = account_dao

    def service_create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning SAL method create account")
        pass

    def service_get_account_by_id(self, account_id: int) -> BankAccount:
        logging.info("Beginning SAL method get account by ID")
        pass

    def service_get_all_accounts(self, customer_id: int) -> List[BankAccount]:
        logging.info("Beginning SAL method get all accounts")
        pass

    def service_deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        logging.info("Beginning SAL method deposit")
        pass

    def service_withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        logging.info("Beginning SAL method withdraw")
        pass

    def service_transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        logging.info("Beginning SAL method transfer")
        pass

    def service_delete_account(self, account_id: int) -> bool:
        logging.info("Beginning SAL method delete account")
        pass
