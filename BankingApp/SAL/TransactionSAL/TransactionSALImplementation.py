import logging
from typing import List

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Transaction import Transaction
from BankingApp.SAL.TransactionSAL.TransactionSALInterface import TransactionSALInterface

account_dao = BankAccountDALImplementation()

class TransactionSALImplementation(TransactionSALInterface):

    def __init__(self, transaction_dao: TransactionDALImplementation):
        self.transaction_dao = transaction_dao

    def service_create_transaction(self, transaction: Transaction) -> Transaction:
        logging.info("Beginning SAL method create transaction")
        if type(transaction.date_time) != str:
            logging.info("SAL method create transaction, date and time not a string")
            raise FailedTransaction("The date and time field must be a string, please try again!")
        elif len(transaction.date_time) > 26:
            logging.warning("SAL method create transaction, date and time longer than 26 characters")
            raise FailedTransaction("The date and time field cannot exceed 26 characters, please try again!")
        elif len(transaction.date_time) == 0:
            logging.warning("SAL method create transaction, date and time left empty")
            raise FailedTransaction("The date and time field cannot be left empty, please try again!")
        elif type(transaction.transaction_type) != str:
            logging.warning("SAL method create transaction, transaction type not a string")
            raise FailedTransaction("The transaction type field must be a string, please try again!")
        elif len(transaction.transaction_type) > 8:
            logging.warning("SAL method create transaction, transaction type longer than 8 characters")
            raise FailedTransaction("The transaction type field cannot exceed 8 characters, please try again!")
        elif len(transaction.transaction_type) == 0:
            logging.warning("SAL method create transaction, transaction type left empty")
            raise FailedTransaction("The transaction type field cannot be left empty, please try again!")
        elif type(transaction.account_id) != int:
            logging.warning("SAL method create transaction, account ID not an integer")
            raise FailedTransaction("The account ID field must be an integer, please try again!")
        elif type(transaction.amount) != float:
            logging.warning("SAL method create transaction, transaction amount not a float")
            raise FailedTransaction("The transaction amount field must be a float, please try again!")
        elif transaction.amount < 0.00:
            logging.warning("SAL method create transaction, transaction amount negative")
            raise FailedTransaction("The transaction amount field cannot be negative, please try again!")
        else:
            valid_account_check = account_dao.get_account_by_id(transaction.account_id)
            if valid_account_check is not None:
                result = self.transaction_dao.create_transaction(transaction)
                logging.info("Finishing SAL method create transaction")
                return result

    def service_get_transaction_by_id(self, transaction_id: int) -> Transaction:
        logging.info("Beginning SAL method get transaction by ID")
        result = self.transaction_dao.get_transaction_by_id(transaction_id)
        logging.info("Finishing SAL method get transaction by ID")
        return result

    def service_get_all_transactions(self, account_id: int) -> List[Transaction]:
        logging.info("Beginning SAL method get all transactions")
        transaction_list = self.transaction_dao.get_all_transactions(account_id)
        if transaction_list is None:
            logging.warning("SAL method get all transactions, no transactions found")
            raise FailedTransaction("No transactions found, please try again!")
        else:
            logging.info("Finishing SAL method get all transactions")
            return transaction_list

    def service_delete_transaction(self, transaction_id: int) -> bool:
        logging.info("Beginning SAL method delete transaction")
        valid_transaction_check = self.transaction_dao.get_transaction_by_id(transaction_id)
        if valid_transaction_check is not None:
            result = self.transaction_dao.delete_transaction(transaction_id)
            logging.info("Finishing SAL method delete transaction")
            return result

    def service_delete_all_transactions(self, account_id: int) -> bool:
        logging.info("Beginning SAL method delete all transactions")
        result = self.transaction_dao.delete_all_transactions(account_id)
        logging.info("Finishing SAL method delete all transactions")
        return result
