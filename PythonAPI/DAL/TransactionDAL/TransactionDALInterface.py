from abc import ABC, abstractmethod
from typing import List
from PythonAPI.Entities.Transaction import Transaction

class TransactionDALInterface(ABC):

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        pass

    @abstractmethod
    def get_all_transactions(self, account_id: int) -> List[Transaction]:
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_transactions(self, account_id: int) -> bool:
        pass
