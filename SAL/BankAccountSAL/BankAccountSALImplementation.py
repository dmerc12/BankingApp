import logging
from typing import List
from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.BankAccount import BankAccount
from Entities.FailedTransaction import FailedTransaction
from SAL.BankAccountSAL.BankAccountSALInterface import BankAccountSALInterface
from SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation


class BankAccountSALImplementation(BankAccountSALInterface):
    transaction_dao = TransactionDALImplementation()
    transaction_sao = TransactionSALImplementation(transaction_dao)

    def __init__(self, account_dao: BankAccountDALImplementation):
        self.account_dao = account_dao

    def service_create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning SAL method create account")
        if account.balance < 0.00:
            logging.warning("SAL method create account, negative balance attempted")
            raise FailedTransaction("The balance field cannot be negative, please try again!")
        else:
            new_account = self.account_dao.create_account(account)
            logging.info("Finishing SAL method create account")
            return new_account

    def service_get_account_by_id(self, account_id: str) -> BankAccount:
        logging.info("Beginning SAL method get account by ID")
        if account_id == "":
            logging.warning("SAL method get account by ID, account ID left empty")
            raise FailedTransaction("The account ID field cannot be left empty, please try again!")
        else:
            account_id = int(account_id)
            account = self.account_dao.get_account_by_id(account_id)
            logging.info("Finishing SAL method get account by ID")
            return account

    def service_get_all_accounts(self, customer_id: str) -> List[str]:
        logging.info("Beginning SAL method get all accounts")
        if customer_id == "":
            logging.warning("SAL method get all accounts, customer ID left empty")
            raise FailedTransaction("The customer ID field cannot be left empty, please try again!")
        else:
            customer_id = int(customer_id)
            account_list = self.account_dao.get_all_accounts(customer_id)
            logging.info("Finishing SAL method get all accounts")
            return account_list

    def service_deposit(self, account_id: str, deposit_amount: str) -> BankAccount:
        logging.info("Beginning SAL method deposit")
        if account_id == "":
            logging.warning("SAL method deposit, account ID left empty")
            raise FailedTransaction("The deposit account ID field cannot be left empty, please try again!")
        else:
            if deposit_amount == "":
                logging.warning("SAL method deposit, deposit amount left empty")
                raise FailedTransaction("The deposit amount field cannot be left empty, please try again!")
            else:
                account_id_integer = int(account_id)
                deposit_amount = float(deposit_amount)
                self.account_dao.get_account_by_id(account_id_integer)
                if deposit_amount <= 0.00:
                    logging.warning("SAL method deposit, deposit amount negative or 0")
                    raise FailedTransaction("The deposit amount field cannot be negative or 0.00, please try again!")
                else:
                    deposit_result = self.account_dao.deposit(account_id_integer, deposit_amount)
                    logging.info("Finishing SAL method deposit")
                    return deposit_result

    def service_withdraw(self, account_id: str, withdraw_amount: str) -> BankAccount:
        logging.info("Beginning SAL method withdraw")
        if account_id == "":
            logging.warning("SAL method withdraw, account ID left empty")
            raise FailedTransaction("The withdraw account ID field cannot be left empty, please try again!")
        else:
            if withdraw_amount == "":
                logging.warning("SAL method withdraw, withdraw amount left empty")
                raise FailedTransaction("The withdraw amount field cannot be left empty, please try again!")
            else:
                account_id = int(account_id)
                withdraw_amount = float(withdraw_amount)
                self.account_dao.get_account_by_id(account_id)
                if withdraw_amount <= 0.00:
                    logging.warning("SAL method withdraw, withdraw amount negative")
                    raise FailedTransaction("The withdraw amount field cannot be negative or 0.00, please try again!")
                else:
                    current_account_balance = self.account_dao.get_account_by_id(account_id).balance
                    if (current_account_balance - withdraw_amount) < 0:
                        logging.warning("SAL method withdraw, insufficient funds")
                        raise FailedTransaction("Insufficient funds, please try again!")
                    else:
                        updated_account_info = self.account_dao.deposit(account_id, withdraw_amount)
                        logging.info("Finishing SAL method withdraw")
                        return updated_account_info

    def service_transfer(self, withdraw_account_id: str, deposit_account_id: str, transfer_amount: str) -> bool:
        logging.info("Beginning SAL method transfer")
        if withdraw_account_id == "":
            logging.warning("SAL method transfer, withdraw account ID left empty")
            raise FailedTransaction("The withdraw account ID field cannot be left empty, please try again!")
        else:
            if deposit_account_id == "":
                logging.warning("SAL method transfer, deposit account ID left empty")
                raise FailedTransaction("The deposit account ID field cannot be left empty, please try again!")
            else:
                if transfer_amount == "":
                    logging.warning("SAL method transfer, transfer amount left empty")
                    raise FailedTransaction("The transfer field cannot be left empty, please try again!")
                else:
                    withdraw_account_id = int(withdraw_account_id)
                    deposit_account_id = int(deposit_account_id)
                    transfer_amount = float(transfer_amount)
                    self.account_dao.get_account_by_id(withdraw_account_id)
                    self.account_dao.get_account_by_id(deposit_account_id)
                    if transfer_amount <= 0.00:
                        logging.warning("SAL method transfer, transfer amount negative")
                        raise FailedTransaction("The transfer amount field cannot be negative or 0.00, "
                                                "please try again!")
                    else:
                        current_withdraw_account_info = self.account_dao.get_account_by_id(withdraw_account_id)
                        if (current_withdraw_account_info.balance - transfer_amount) < 0.00:
                            logging.warning("SAL method transfer, insufficient funds")
                            raise FailedTransaction("Insufficient funds, please try again!")
                        else:
                            result = self.account_dao.transfer(withdraw_account_id, deposit_account_id, transfer_amount)
                            logging.info("Finishing SAL method transfer")
                            return result

    def service_delete_account(self, account_id: str) -> bool:
        logging.info("Beginning SAL method delete account")
        if account_id == "":
            logging.warning("SAL method delete account, account ID left empty")
            raise FailedTransaction("The account ID field cannot be left empty, please try again!")
        else:
            account_id = int(account_id)
            self.account_dao.get_account_by_id(account_id)
            self.transaction_sao.service_delete_all_transactions(account_id)
            result = self.account_dao.delete_account(account_id)
            logging.info("Finishing SAL method delete account")
            return result
