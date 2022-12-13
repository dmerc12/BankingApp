import logging
from typing import List

from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation
from Entities.Transaction import Transaction
from SAL.TransactionSAL.TransactionSALInterface import TransactionSALInterface


class TransactionSALImplementation(TransactionSALInterface):

    def __init__(self, transaction_dao: TransactionDALImplementation):
        self.transaction_dao = transaction_dao

    def service_create_transaction(self, transaction: Transaction) -> Transaction:
        logging.info("Beginning SAL method create transaction")
        logging.info("Finishing SAL method create transaction")
        return transaction

    def service_get_transaction_by_id(self, transaction_id: int) -> Transaction:
        logging.info("Beginning SAL method get transaction by ID")
        result = self.transaction_dao.get_transaction_by_id(transaction_id)
        logging.info("Finishing SAL method get transaction by ID")
        return result

    def service_get_all_transactions(self, account_id: int) -> List[Transaction]:
        logging.info("Beginning SAL method get all transactions")
        transaction_list = []
        logging.info("Finishing SAL method get all transactions")
        return transaction_list

    def service_delete_transaction(self, transaction_id: int) -> bool:
        logging.info("Beginning SAL method delete transaction")
        result = self.transaction_dao.delete_transaction(transaction_id)
        logging.info("Finishing SAL method delete transaction")
        return result
