from typing import List
from DAL.DBConnection import connection
from DAL.TransactionDAL.TransactionDALInterface import TransactionDALInterface
from Entities.Transaction import Transaction

class TransactionDALImplementation(TransactionDALInterface):

    @staticmethod
    def truncate_transaction_table(sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
        return True

    def create_transaction(self, transaction: Transaction) -> Transaction:
        pass

    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        pass

    def get_all_transactions(self, account_id: int) -> List[Transaction]:
        pass

    def delete_transaction(self, transaction_id: int) -> bool:
        pass
