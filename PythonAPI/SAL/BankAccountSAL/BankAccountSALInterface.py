from abc import ABC, abstractmethod
from typing import List

from Entities.BankAccount import BankAccount


class BankAccountSALInterface(ABC):

    @abstractmethod
    def service_create_account(self, account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id: str) -> BankAccount:
        pass

    @abstractmethod
    def service_get_all_accounts(self, customer_id: str) -> List[str]:
        pass

    @abstractmethod
    def service_deposit(self, account_id: str, deposit_amount: str) -> BankAccount:
        pass

    @abstractmethod
    def service_withdraw(self, account_id: str, withdraw_amount: str) -> BankAccount:
        pass

    @abstractmethod
    def service_transfer(self, withdraw_account_id: str, deposit_account_id: str, transfer_amount: str) -> bool:
        pass

    @abstractmethod
    def service_delete_account(self, account_id: str) -> bool:
        pass
