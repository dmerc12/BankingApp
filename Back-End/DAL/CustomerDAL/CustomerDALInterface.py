from abc import ABC, abstractmethod

from Entities.Customer import Customer


class CustomerDALInterface(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_email(self, email: str) -> Customer:
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> Customer:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def change_password(self, customer_id: int, new_password: str) -> bool:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> bool:
        pass
