from abc import ABC, abstractmethod
from typing import List

from Entities.BankAccount import BankAccount

class BankAccountSALInterface(ABC):

    @abstractmethod
    def service_create_account(self, account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def service_get_all_accounts(self, customer_id: int) -> List[BankAccount]:
        pass

    @abstractmethod
    def service_deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def service_withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def service_transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        pass

    @abstractmethod
    def service_delete_account(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_delete_all_accounts(self, customer_id: int) -> bool:
        pass
