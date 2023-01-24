from abc import ABC, abstractmethod
from typing import List

from PythonAPI.Entities.Transaction import Transaction


class TransactionSALInterface(ABC):

    @abstractmethod
    def service_create_transaction(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def service_get_transaction_by_id(self, transaction_id: int) -> Transaction:
        pass

    @abstractmethod
    def service_get_all_transactions(self, account_id: int) -> List[Transaction]:
        pass

    @abstractmethod
    def service_delete_transaction(self, transaction_id: int) -> bool:
        pass

    @abstractmethod
    def service_delete_all_transactions(self, account_id: int) -> bool:
        pass
