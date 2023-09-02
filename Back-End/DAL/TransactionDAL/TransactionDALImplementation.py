import logging
from typing import List

from DAL.TransactionDAL.TransactionDALInterface import TransactionDALInterface
from Database.config import Connect
from Entities.Transaction import Transaction

class TransactionDALImplementation(TransactionDALInterface):

    def create_transaction(self, transaction: Transaction) -> Transaction:
        logging.info("Beginning DAL method create transaction")
        sql = "insert into banking.transactions values (default, %s, %s, %s, %s) returning transaction_id;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, (transaction.date_time, transaction.transaction_type, transaction.account_id,
                             transaction.amount))
        Connect.connection.commit()
        transaction_id = cursor.fetchone()[0]
        transaction.transaction_id = transaction_id
        logging.info("Finishing DAL method create transaction")
        return transaction

    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        logging.info("Beginning DAL method get transaction by ID")
        sql = "select * from banking.transactions where transaction_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [transaction_id])
        transaction_info = cursor.fetchone()
        if transaction_info is None:
            logging.warning("DAL method get transaction by ID, transaction not found")
            return None
        transaction = Transaction(*transaction_info)
        logging.info("Finishing DAL method get transaction by ID")
        return transaction

    def get_all_transactions(self, account_id: int) -> List[Transaction]:
        logging.info("Beginning DAL method get all transactions")
        sql = "select * from banking.transactions where account_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [account_id])
        transaction_records = cursor.fetchall()
        transaction_list = []
        for transaction in transaction_records:
            transaction = Transaction(*transaction)
            transaction_list.append(transaction)
        logging.info("Finishing DAL method get all transactions")
        return transaction_list

    def delete_transaction(self, transaction_id: int) -> bool:
        logging.info("Beginning DAL method delete transaction")
        sql = "delete from banking.transactions where transaction_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [transaction_id])
        Connect.connection.commit()
        logging.info("Finishing DAL method delete transaction")
        return True

    def delete_all_transactions(self, account_id) -> bool:
        logging.info("Beginning DAL method delete all transactions")
        sql = "delete from banking.transactions where account_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [account_id])
        Connect.connection.commit()
        logging.info("Finishing DAL method delete all transactions")
        return True
