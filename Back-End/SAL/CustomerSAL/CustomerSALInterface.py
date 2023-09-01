from abc import ABC, abstractmethod

from Entities.Customer import Customer

class CustomerSALInterface(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer, password_confirmation: str) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_email(self, email: str) -> Customer:
        pass

    @abstractmethod
    def service_login(self, email: str, password: str) -> Customer:
        pass

    @abstractmethod
    def service_update_customer(self, customer: Customer, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_change_password(self, customer_id: int, new_password: str, password_confirmation: str) -> bool:
        pass

    @abstractmethod
    def service_delete_customer(self, customer_id: int) -> bool:
        pass
