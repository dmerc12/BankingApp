import logging
from typing import List
from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.BankAccount import BankAccount
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALInterface import BankAccountSALInterface
from BankingApp.SAL.TransactionSAL.TransactionSALImplementation import TransactionSALImplementation


class BankAccountSALImplementation(BankAccountSALInterface):

    transaction_dao = TransactionDALImplementation()
    transaction_sao = TransactionSALImplementation(transaction_dao)

    def __init__(self, account_dao: BankAccountDALImplementation):
        self.account_dao = account_dao

    def service_create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning SAL method create account with data: " +
                     str(account.convert_to_dictionary()))
        if account.balance < 0.00:
            logging.warning("SAL method create account, negative balance attempted")
            raise FailedTransaction("The balance field cannot be negative, please try again!")
        else:
            new_account = self.account_dao.create_account(account)
            logging.info("Finishing SAL method create account with result: " +
                         str(new_account.convert_to_dictionary()))
            return new_account

    def service_get_account_by_id(self, account_id: str) -> BankAccount:
        logging.info("Beginning SAL method get account by ID with account ID: " + str(account_id))
        if account_id == "":
            logging.warning("SAL method get account by ID, account ID left empty")
            raise FailedTransaction("The account ID field cannot be left empty, please try again!")
        else:
            account_id = int(account_id)
            account = self.account_dao.get_account_by_id(account_id)
            logging.info("Finishing SAL method get account by ID: " +
                         str(account.convert_to_dictionary()))
            return account

    def service_get_all_accounts(self, customer_id: str) -> List[BankAccount]:
        logging.info("Beginning SAL method get all accounts with customer ID: " + str(customer_id))
        if customer_id == "":
            logging.warning("SAL method get all accounts, customer ID left empty")
            raise FailedTransaction("The customer ID field cannot be left empty, please try again!")
        else:
            customer_id = int(customer_id)
            account_list = self.account_dao.get_all_accounts(customer_id)
            for account in account_list:
                logging.info("Finishing SAL method get all accounts with account: " +
                             str(account.convert_to_dictionary()))
            return account_list

    def service_get_accounts_for_delete(self, customer_id: int) -> List[BankAccount]:
        logging.info("Beginning SAL method get accounts for delete with customer ID: " + str(customer_id))
        if type(customer_id) != int:
            logging.warning("SAL method get accounts for delete, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            account_list = self.account_dao.get_accounts_for_delete(customer_id)
            for account in account_list:
                logging.info("Finishing SAL method get all accounts with account: " +
                             str(account.convert_to_dictionary()))
            return account_list

    def service_deposit(self, account_id: str, deposit_amount: str) -> BankAccount:
        logging.info("Beginning SAL method deposit with deposit account ID: " + str(account_id) +
                     ", and deposit amount: " + str(deposit_amount))
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
                    logging.info("Finishing SAL method deposit with result: " +
                                 str(deposit_result.convert_to_dictionary()))
                    return deposit_result

    def service_withdraw(self, account_id: str, withdraw_amount: str) -> BankAccount:
        logging.info("Beginning SAL method withdraw with withdraw account ID: " + str(account_id) +
                     ", and withdraw amount: " + str(withdraw_amount))
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
                        updated_account_info = self.account_dao.withdraw(account_id, withdraw_amount)
                        logging.info("Finishing SAL method withdraw with result: " +
                                     str(updated_account_info.convert_to_dictionary()))
                        return updated_account_info

    def service_transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        logging.info("Beginning SAL method transfer with withdraw account ID: " + str(withdraw_account_id) +
                     ", and deposit account ID: " + str(deposit_account_id) + ", and transfer amount: " +
                     str(transfer_amount))
        if type(withdraw_account_id) != int:
            logging.warning("SAL method transfer, withdraw account ID not integer")
            raise FailedTransaction("The withdraw account ID field must be an integer, please try again!")
        else:
            if type(deposit_account_id) != int:
                logging.warning("SAL method transfer, deposit account ID not integer")
                raise FailedTransaction("The deposit account ID field must be an integer, please try again!")
            else:
                if type(transfer_amount) != float:
                    logging.warning("SAL method transfer, transfer amount not float")
                    raise FailedTransaction("The transfer field must be a float, please try again!")
                else:
                    if withdraw_account_id == deposit_account_id:
                        logging.warning("SAL method transfer, deposit and withdraw accounts the same")
                        raise FailedTransaction("The deposit and withdraw accounts cannot be the same, "
                                                "please try again!")
                    else:
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
        logging.info("Beginning SAL method delete account with account ID: " + str(account_id))
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

    def service_delete_all_accounts(self, customer_id: str) -> bool:
        logging.info("Beginning SAL method delete all accounts with customer ID: " + str(customer_id))
        if customer_id == "":
            logging.warning("SAL method delete all accounts, customer ID left empty")
            raise FailedTransaction("The customer ID field cannot be left empty!, please try again!")
        else:
            customer_id = int(customer_id)
            self.account_dao.delete_all_accounts(customer_id)
            return True


