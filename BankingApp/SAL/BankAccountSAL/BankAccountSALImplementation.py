import logging
from typing import List
from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.Entities.BankAccount import BankAccount
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.SAL.BankAccountSAL.BankAccountSALInterface import BankAccountSALInterface
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation


class BankAccountSALImplementation(BankAccountSALInterface):
    customer_dao = CustomerDALImplementation()
    customer_sao = CustomerSALImplementation(customer_dao)

    def __init__(self, account_dao: BankAccountDALImplementation):
        self.account_dao = account_dao

    def service_create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning SAL method create account with data: " +
                     str(account.convert_to_dictionary()))
        if type(account.balance) != float:
            logging.warning("SAL method create account, account balance not a float")
            raise FailedTransaction("The balance field must be a float, please try again!")
        elif type(account.customer_id) != int:
            logging.warning("SAL method create account, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        elif account.balance < 0.00:
            logging.warning("SAL method create account, negative balance attempted")
            raise FailedTransaction("The balance field cannot be negative, please try again!")
        else:
            self.customer_sao.service_get_customer_by_id(account.customer_id)
            new_account = self.account_dao.create_account(account)
            logging.info("Finishing SAL method create account with result: " +
                         str(new_account.convert_to_dictionary()))
            return new_account

    def service_get_account_by_id(self, account_id: int) -> BankAccount:
        logging.info("Beginning SAL method get account by ID with account ID: " + str(account_id))
        if type(account_id) != int:
            logging.warning("SAL method get account by ID, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        else:
            account = self.account_dao.get_account_by_id(account_id)
            if account is None:
                logging.warning("SAL method get account by ID, no account found")
                raise FailedTransaction("This account cannot be found, please try again!")
            else:
                logging.info("Finishing SAL method get account by ID: " +
                             str(account.convert_to_dictionary()))
                return account

    def service_get_all_accounts(self, customer_id: int) -> List[BankAccount]:
        logging.info("Beginning SAL method get all accounts with customer ID: " + str(customer_id))
        if type(customer_id) != int:
            logging.warning("SAL method get all accounts, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            customer_id = int(customer_id)
            account_list = self.account_dao.get_all_accounts(customer_id)
            if len(account_list) == 0:
                logging.warning("SAL method get all accounts, no accounts found")
                raise FailedTransaction("No accounts found, please try again!")
            else:
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

    def service_deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        logging.info("Beginning SAL method deposit with deposit account ID: " + str(account_id) +
                     ", and deposit amount: " + str(deposit_amount))
        if type(account_id) != int:
            logging.warning("SAL method deposit, account ID not an integer")
            raise FailedTransaction("The deposit account ID field must be an integer, please try again!")
        elif type(deposit_amount) != float:
            logging.warning("SAL method deposit, deposit amount not a float")
            raise FailedTransaction("The deposit amount field must be a float, please try again!")
        else:
            self.service_get_account_by_id(account_id)
            if deposit_amount <= 0.00:
                logging.warning("SAL method deposit, deposit amount negative or 0")
                raise FailedTransaction("The deposit amount field cannot be negative or 0.00, please try again!")
            else:
                deposit_result = self.account_dao.deposit(account_id, deposit_amount)
                logging.info("Finishing SAL method deposit with result: " +
                             str(deposit_result.convert_to_dictionary()))
                return deposit_result

    def service_withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        logging.info("Beginning SAL method withdraw with withdraw account ID: " + str(account_id) +
                     ", and withdraw amount: " + str(withdraw_amount))
        if type(account_id) != int:
            logging.warning("SAL method withdraw, account ID not an integer")
            raise FailedTransaction("The withdraw account ID field must be an integer, please try again!")
        elif type(withdraw_amount) != float:
            logging.warning("SAL method withdraw, withdraw amount not float")
            raise FailedTransaction("The withdraw amount field must be a float, please try again!")
        else:
            current_information = self.service_get_account_by_id(account_id)
            if withdraw_amount <= 0.00:
                logging.warning("SAL method withdraw, withdraw amount negative")
                raise FailedTransaction("The withdraw amount field cannot be negative or 0.00, please try again!")
            else:
                current_account_balance = current_information.balance
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
        elif type(deposit_account_id) != int:
            logging.warning("SAL method transfer, deposit account ID not integer")
            raise FailedTransaction("The deposit account ID field must be an integer, please try again!")
        elif type(transfer_amount) != float:
            logging.warning("SAL method transfer, transfer amount not float")
            raise FailedTransaction("The transfer field must be a float, please try again!")
        elif withdraw_account_id == deposit_account_id:
            logging.warning("SAL method transfer, deposit and withdraw accounts the same")
            raise FailedTransaction("The deposit and withdraw accounts cannot be the same, please try again!")
        elif transfer_amount <= 0.00:
            logging.warning("SAL method transfer, transfer amount negative")
            raise FailedTransaction("The transfer amount field cannot be negative or 0.00, please try again!")
        else:
            current_withdraw_account_information = self.service_get_account_by_id(withdraw_account_id)
            self.service_get_account_by_id(deposit_account_id)
            if (current_withdraw_account_information.balance - transfer_amount) < 0.00:
                logging.warning("SAL method transfer, insufficient funds")
                raise FailedTransaction("Insufficient funds, please try again!")
            else:
                result = self.account_dao.transfer(withdraw_account_id, deposit_account_id, transfer_amount)
                logging.info("Finishing SAL method transfer")
                return result

    def service_delete_account(self, account_id: int) -> bool:
        logging.info("Beginning SAL method delete account with account ID: " + str(account_id))
        if type(account_id) != int:
            logging.warning("SAL method delete account, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        else:
            self.service_get_account_by_id(account_id)
            # need to move the below transaction sao and anything else needed to API layer
            # self.transaction_sao.service_delete_all_transactions(account_id)
            result = self.account_dao.delete_account(account_id)
            logging.info("Finishing SAL method delete account")
            return result

    def service_delete_all_accounts(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete all accounts with customer ID: " + str(customer_id))
        if type(customer_id) != int:
            logging.warning("SAL method delete all accounts, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        else:
            customer_id = int(customer_id)
            self.account_dao.delete_all_accounts(customer_id)
            return True


