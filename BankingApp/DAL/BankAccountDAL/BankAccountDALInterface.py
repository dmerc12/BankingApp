from abc import ABC, abstractmethod
from typing import List
from BankingApp.Entities.BankAccount import BankAccount

class BankAccountDALInterface(ABC):

    @abstractmethod
    def create_account(self, account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def get_all_accounts(self, customer_id: int) -> List[BankAccount]:
        pass

    @abstractmethod
    def get_accounts_for_delete(self, customer_id: int) -> List[BankAccount]:
        pass

    @abstractmethod
    def deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        pass

    @abstractmethod
    def delete_account(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_accounts(self, customer_id: int) -> bool:
        pass
